from docutils import nodes
from docutils.parsers.rst import directives

TEMPLATE ="""                                                                                                                                                                                                                                  
  <table>                                                                                                                                                                                                                                      
    <tr>                                                                                                                                                                                                                                       
      <td valign="middle" align="center">                                                                                                                                                                                                      
        <video src="%(filename)s" width="%(width)s" height="%(height)s" controls>                                                                                                                                                              
        </video>                                                                                                                                                                                                                               
      </td>                                                                                                                                                                                                                                    
    </tr>                                                                                                                                                                                                                                      
  </table>                                                                                                                                                                                                                                     
"""

def video(name, args, options, content, lineno,
            contentOffset, blockText, state, stateMachine):
    if len(content) == 0:
        return
    template_vars = { #Set the defaults if none of specified                                                                                                                                                                                   
        'filename': content[0],
        'width': 800,
        'height': 600
    }
    extra_args = content[1:] # Because content[0] is ID                                                                                                                                                                                        
    extra_args = [ea.strip().split("=") for ea in extra_args] # key=value                                                                                                                                                                      
    extra_args = [ea for ea in extra_args if len(ea) == 2] # drop bad lines                                                                                                                                                                    
    extra_args = dict(extra_args)
    if 'width' in extra_args:
        template_vars['width'] = extra_args.pop('width')
    if 'height' in extra_args:
        template_vars['height'] = extra_args.pop('height')
    return  [nodes.raw('', TEMPLATE % (template_vars), format='html')]

video.content = True
directives.register_directive('video',video)


