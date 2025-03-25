---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.16.7
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

```{code-cell} ipython3
from pathlib import Path
import pandas as pd


data_dir = Path('..', 'data', 'derived')
df = (
    pd.read_csv(data_dir / 'weather.csv')
    .assign(
        time=lambda df: pd.to_datetime(df['time'], format='%Y-%m-%dT%H:%M'),
        year=lambda d: d['time'].dt.year,
        month=lambda d: d['time'].dt.month,
        day=lambda d: d['time'].dt.day,
    )
)

df.head()
```

## Exploratory Viz

### All Data

```{code-cell} ipython3
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(12, 3))
ax.plot(df['time'], df['temperature_2m (°F)'])
```

### Daily Smoothing

```{code-cell} ipython3
daily_df = (
    df.set_index('time')
    .resample('D')['temperature_2m (°F)']
    .agg(['mean', 'std'])
    .reset_index()
)

fig, ax = plt.subplots(figsize=(12, 3))
ax.plot(daily_df['time'], daily_df['mean'])
```

### Yearly Smoothing

```{code-cell} ipython3
yearly_df = (
    df.set_index('time')
    .resample('365D')['temperature_2m (°F)']
    .agg(['mean', 'std']).reset_index()
)

fig, ax = plt.subplots(figsize=(12, 3))
ax.plot('time', 'mean', data=yearly_df)
```

## Visual Set Up

```{code-cell} ipython3
from pandas import Timestamp

reference_dates = Timestamp(1950, 1, 1), Timestamp(1989, 12, 31)
comparison_year = 2024
```

```{code-cell} ipython3
ref_df = (
    df.loc[lambda d: d['time'].between(*reference_dates)]
    .resample('D', on='time').mean()
    .groupby(['month', 'day'])
    .agg(
        lb=('temperature_2m (°F)', lambda g: g.quantile(0.05)),
        ub=('temperature_2m (°F)', lambda g: g.quantile(0.95)),
        mean=('temperature_2m (°F)', 'mean'),
    )
    .add_prefix('temp_ref_')
)

ref_df
```

```{code-cell} ipython3
plot_df = (
    df.loc[lambda d: d['time'].dt.year == comparison_year]
    .resample('D', on='time').mean()
    .merge(ref_df, left_on=['month', 'day'], right_index=True)
    .assign(
        distance=lambda d: (
            d['temperature_2m (°F)'] - d['temp_ref_mean']
        ).pipe(lambda s: s / s.abs().max())
                                                                              
    )
    .reset_index()
)

plot_df
```

```{code-cell} ipython3
#| label: viz
plt.rc('font', size=14)

fig, ax = plt.subplots(figsize=(16, 6))

ax.plot('time', 'temp_ref_ub', data=plot_df, color='k', lw=.6)
ax.plot('time', 'temp_ref_lb', data=plot_df, color='k', lw=.6)
ax.fill_between(
    'time', 'temp_ref_ub', 'temp_ref_lb', data=plot_df, color='gainsboro', zorder=5, ec='none', alpha=.6
)
ax.plot('time', 'temp_ref_mean', data=plot_df, color='k', zorder=6)

raw_pc = ax.fill_between(
    'time', 'temperature_2m (°F)', 'temp_ref_mean', data=plot_df,
    zorder=5, ec=ax.get_facecolor(),
    fc='none',
)

arr = raw_pc.get_paths()[0].vertices
(x0, y0), (x1, y1) = arr.min(axis=0), arr.max(axis=0)

gradient = ax.imshow(
    plot_df[['distance']].T,
    extent=[x0, x1, y0, y1],
    aspect='auto',
    cmap='RdBu_r',
    vmin=-1,
    vmax=1,
    zorder=5,
)

gradient.set_clip_path(raw_pc.get_paths()[0], transform=ax.transData)
```
