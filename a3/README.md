# Tasks
Look at the tasks to make sure everything is done as described.

## Exercise 2: Visualization with Seaborn for Exploratory Data Analysis

### Data Cleaning
- [ ] Count NaN values in each column
- [ ] Drop all rows containing NaN values
- [ ] Find unique values for `species` and `island`, and min/max/mean for numeric columns

### Plotting Data Distributions
- [ ] Produce a histogram of penguins' body mass (Pandas API)
- [ ] Produce a histogram of penguins' body mass (Seaborn API)
- [ ] Produce a histogram of body mass conditioned on sex (hue)
- [ ] Try different variables for histograms (e.g., bill length, species)
- [ ] Turn a histogram into a KDE plot

### Plotting Relationships Between Variables
- [ ] Scatter plot: bill length vs. body mass
- [ ] Scatter plot: bill length vs. body mass, colored by species
- [ ] Linear regression: bill length vs. body mass (simple)
- [ ] Linear regression: bill length vs. body mass, conditioned on species
- [ ] Facet grid: scatter plot by sex

### Plotting Categorical Data
- [ ] Categorical scatter plot: species vs. bill length
- [ ] Box plot: species vs. bill length
- [ ] Bar plot (count plot): penguin count by island and species

### Plotting Time Series Data
- [ ] Line plot: date vs. sales
- [ ] Line plot: date vs. sales, profit, and expenses (wide-form data)

---

## Exercise 3: Making High-Quality Seaborn Visualizations

### Controlling Figure Aesthetics (Line Plot)
- [ ] Change plot style: white background, ticks, remove top/right spines
- [ ] Make plot larger, increase font and line thickness, adjust legend
- [ ] Set y-axis major ticks every 50, minor ticks every 10
- [ ] Turn off error band plotting
- [ ] Add markers for data points, make all lines solid

### Categorical Plots & Facet Grids (Yu-Gi-Oh Dataset)
- [ ] Scatter plot: attack vs. defense, colored by level, use `flare` palette
- [ ] Set minor ticks every 100 on axes, change axis labels, show all 8 levels in legend, move legend outside plot
- [ ] FacetGrid: scatter plot by Attributes, custom column titles
- [ ] Assign individual colors to monster Attributes in strip plot

---

## Exercise 9: Data Visualization with ggplot2, Continued

### Customizing Plots (Yu-Gi-Oh Dataset)
- [ ] Show "Level" in color and increase point size in scatter plot
- [ ] Add title, subtitle, caption, and custom axis/legend labels
- [ ] Set x/y axis range [0, 3000], major ticks every 500, minor every 100
- [ ] Change color scale to non-blue, darker for higher level
- [ ] Change theme and aspect ratio (make plot wider)
- [ ] Annotate and circle selected data points
- [ ] Make "Level" legend discrete (not gradient)

### Coffee Chain Visualization
- [ ] Plot average sales, profits, and expenses per day (lines by color and style, x-axis labels every 3 months, y-axis 0–400, major ticks 50, minor 10)
- [ ] Plot same as above, but add confidence intervals (error bands)
