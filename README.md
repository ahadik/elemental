<style>
	.element {
		border: 1px solid black;
		display: -webkit-box;
		display: -ms-flexbox;
		display: flex;
		-webkit-box-orient: vertical;
		-webkit-box-direction: normal;
		-ms-flex-direction: column;
		flex-direction: column;
		font-family: sans-serif;
		padding: 1%; }
	.element .element__atomic-number {
		-ms-flex-preferred-size: 0;
		flex-basis: 0;
		width: 100%; }
	.element .element__symbol {
		-ms-flex-preferred-size: 100%;
	    flex-basis: 100%;
		line-height: 1em;
		text-align: center;
		width: 100%; }
	.element .element__atomic-mass {
		-ms-flex-preferred-size: 0;
	    flex-basis: 0;
		text-align: right;
		width: 100%; }

	.element {
	  width: 200px;
	  height: 200px;
	  font-size: 25px; }

	  .element.Aluminum .element__symbol::before, .element.Al .element__symbol::before {
	    content: "Al"; }
	  .element.Aluminum .element__atomic-number::before, .element.Al .element__atomic-number::before {
	    content: "13"; }
	  .element.Aluminum .element__atomic-mass::before, .element.Al .element__atomic-mass::before {
	    content: "26.9815386"; }
</style>

#Elemental
###Bringing the power of SASS to the periodic elements

##What This Is
If you've got a web project that needs to display the blocks of the periodic table, this SASS library makes it easy to do just that. All you need to do is provide some super simple markup, and then make use of either the compiled Elemental CSS or SASS mixins.

##How To Use It

*Markup*
The markup needed for an Elemental element is super simple, and needs only a single class to inject the proper content.

	<div class="element Aluminum">
		<span class="element__atomic-number"></span>
		<span class="element__symbol"></span>
		<span class="element__atomic-mass"></span>
	</div>

Alternatively, you can specify the desired element with the elemen't abbreviated name or symbold:

	<div class="element Al">
		<span class="element__atomic-number"></span>
		<span class="element__symbol"></span>
		<span class="element__atomic-mass"></span>
	</div>

This markup generates the following block provided the proper styling is included:

<div class="element Aluminum">
	<span class="element__atomic-number"></span>
	<span class="element__symbol"></span>
	<span class="element__atomic-mass"></span>
</div>

All data is injected using the `content` CSS attribute. All data is stored inside a SASS map found in `scss/_elements.scss`. You can choose to compile the entire SASS map into CSS (~50kb minified) or import specific elements within your SASS (~4kb per element). SASS usage is explained below.

*CSS*
If you're not a SASS user, you can make use of the full CSS file that comes precompiled with the Bower dependency (`css/elemental.min.css`). You can poke around the unminified CSS by referring to `css/elemental.css`.

To use the pre-compiled CSS file, just include it in your HTML file just as you would any other CSS dependency. This will give you access to the data for all the elements. 

Make note that the pre-compiled CSS is compiled for block dimensions of 100px x 100px. The general rule is that the atomic weight and mass are each given a font height of 1/8 of the block's height and the element's symbol is given a font height of 5/8 of the block's height. You'll need to override these yourself if you want to change the size and use the pre-compiled CSS. The SASS usage has a more elegant interface.

You can change the dimensions by applying your own CSS like so:

	.element{
		width: 200px;
		height: 200px;
		font-size: calc(200px * .125);
	}

Everything else will scale accordingly.


*SASS*
Elemental has a more user-friendly interface for SASS users. You can choose to include (and thus compile) the styling and data for every element, or a subset of them. Although the dimensions can be over-ridden by custom styling, including all elements specifies the same dimensions for every element. Including elements 1 by 1 allows you to specify custom dimensions for each element.

So how to use the SASS library? First of all, include the library in your own SASS styling by importing the `elemental.scss` file. Then, use the `elemental()` mixin to include either all or some of the elements.

The general interface for the `elemental()` mixin is `@mixin elemental($width, $height, $elementList...)`.

The first two arguments are required and specify the width and height of the block. This text will be scaled to fill these dimensions automatically. The final argument, `$elementList...`, is optional and includes all values beyond the first two provided to the `elemental()` mixin. Providing no arguments beyond `$width` and `$height` defaults to including and compiling data for every element.

So, to include all of the elements at once, call the `elemental()` mixin like so:

	@include elemental(100px, 100px);

Or, compile the data for a single element:

	@include elemental(100px, 100px, 'Aluminum')

Or, compile the data for a subset of elements:

	@include elemental(100px, 100px, 'Aluminum', 'Nitrogen')

While you can reference the data and styling for an element in your markup using either the full name (Aluminum) or abbreviation (Al), the `elemental()` mixin requires the full name.

##Contributing
Please feel free to contribute to this repository! Any and all improvements are welcome, be it structural, visual, or just correcting/adding data. This repository works off of two branches, `master` and `distribution`. The `master` branch contains additional scripts and dependencies for working on the project. The `distribution` branch contains only the compiled CSS and source SASS for the bower dependency. Submit PRs for the `master` branch which will be merged into `distribution` once the PR is accepted.
