## render rst file with a html5 reader

The default reader of Pelican for rst file inherits the html4css1 Class from docutils,
this plugin replaces it with the more modern html5_polyglot Class from docutils.
And it will always inserts a `<code></code>` tag within the literal-block `<pre></pre>` tag.
