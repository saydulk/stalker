#-*- coding: utf-8 -*-



import mocker
from stalker.core.models import template






########################################################################
class TemplateTester(mocker.MockerTestCase):
    """tests the template class
    """
    
    
    #----------------------------------------------------------------------
    def setUp(self):
        """setups the tests
        """
        
        # create a proper Template object
        self.kwargs = {
            'name': 'Test Template',
            'description': 'This is a test template',
            'template_code': '{{project.name}}/SEQUENCES/{{sequence.name}}'
        }
        
        self.template_obj = template.Template(**self.kwargs)
    
    
    
    #----------------------------------------------------------------------
    def test_if_template_code_argument_not_accepting_empty_strings(self):
        """testing if assigning an empty string will raise a ValueError
        """
        
        # try to create a new template object with wrong values
        self.kwargs['template_code'] = ''
        self.assertRaises(ValueError, template.Template, **self.kwargs)
    
    
    
    #----------------------------------------------------------------------
    def test_if_template_code_property_not_accepting_empty_strings(self):
        """testing if assigning an empty string will raise a ValueError
        """
        
        # try to assign "" to the template_code property
        self.assertRaises(
            ValueError,
            setattr,
            self.template_obj,
            "template_code",
            ""
        )
    
    
    
    #----------------------------------------------------------------------
    def test_if_template_code_argument_not_acception_None(self):
        """testing if assigning None to template_code raises a ValueError
        """
        # try to create a new template object with wrong values
        self.kwargs['template_code'] = None
        self.assertRaises(ValueError, template.Template, **self.kwargs)
    
    
    
    #----------------------------------------------------------------------
    def test_if_template_code_property_not_acception_None(self):
        """testing if assigning None to template_code raises a ValueError
        """
        # try to assign "" to the template_code property
        self.assertRaises(
            ValueError,
            setattr,
            self.template_obj,
            "template_code",
            None
        )
    
    
    
    #----------------------------------------------------------------------
    def test_if_template_code_argument_accepts_only_strings(self):
        """testing if template_code argument is only accepting string or
        unicode values
        """
        
        test_values = [1, ['template_code']]
        for test_value in test_values:
            self.kwargs['template_code'] = test_value
            # an integer value
            self.assertRaises(ValueError, template.Template, **self.kwargs)
    
    
    
    #----------------------------------------------------------------------
    def test_if_template_code_property_accepts_only_strings(self):
        """testing if template_code property is only accepting string or
        unicode values
        """
        
        test_values = [1, ['template_code']]
        for test_value in test_values:
            # an integer value
            self.assertRaises(
                ValueError,
                setattr,
                self.template_obj,
                "template_code",
                test_value
            )
    
    
    
    #----------------------------------------------------------------------
    def test_if_template_code_property_works(self):
        """testing if template_code property works correctly
        """
        
        test_value = '{{project.name}}/SEQs/{{sequence.name}}/SHOTS/ \
        {{shot.code}}/{{assetType.code'
        
        # lets assign it and check if it is working
        
        self.template_obj.template_code = test_value
        
        self.assertEquals(self.template_obj.template_code, test_value)
    
    
    