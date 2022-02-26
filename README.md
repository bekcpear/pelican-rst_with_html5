## render rst file with a html5 reader

The default reader of Pelican for rst file inherits the html4css1 Class from docutils,
this plugin replaces it with the more modern html5_polyglot Class from docutils.
And it will always wrap a `<code></code>` tag around the literal-block within the `<pre></pre>` tag.

add

```python
PLUGIN_PATHS = ['path/to/your/plugins']
PLUGINS = ['rst_with_html5']
```

to `pelicanconf.py` to use it.
