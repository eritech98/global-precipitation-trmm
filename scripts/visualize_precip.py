import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

# Load the TRMM data
ds = xr.open_dataset("data/trmm_2010_2019.nc")
precip = ds['TRMM_3B42_Daily_7_precipitation']

# Extract latitude and longitude coordinates
lats = precip.lat.values
lons = precip.lon.values

# Create a plot with a global map projection
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection=ccrs.PlateCarree())
ax.set_title("Global Precipitation", fontsize=16)

# Add country borders and land features
ax.add_feature(cfeature.BORDERS, linestyle=':')
ax.add_feature(cfeature.LAND, edgecolor='black', facecolor='lightgray')
ax.add_feature(cfeature.COASTLINE, edgecolor='black')

# Plot the global precipitation data (without using time dimension)
precip.plot(ax=ax, transform=ccrs.PlateCarree(), cmap="Blues", cbar_kwargs={'label': 'Precipitation (mm/day)'})

# Add latitude and longitude gridlines
ax.gridlines(draw_labels=True)

# Save the image
plt.savefig("outputs/static_maps/global_precipitation_with_coords.png", dpi=300)

# Show the plot
plt.show()

print("Global precipitation image with latitudes and longitudes saved.")
