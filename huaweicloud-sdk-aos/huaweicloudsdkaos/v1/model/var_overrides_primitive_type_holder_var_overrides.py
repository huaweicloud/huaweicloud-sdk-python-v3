# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VarOverridesPrimitiveTypeHolderVarOverrides:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vars_uri': 'str',
        'vars_body': 'str',
        'use_stack_set_vars': 'list[str]'
    }

    attribute_map = {
        'vars_uri': 'vars_uri',
        'vars_body': 'vars_body',
        'use_stack_set_vars': 'use_stack_set_vars'
    }

    def __init__(self, vars_uri=None, vars_body=None, use_stack_set_vars=None):
        r"""VarOverridesPrimitiveTypeHolderVarOverrides

        The model defined in huaweicloud sdk

        :param vars_uri: HCL参数文件的OBS地址。HCL模板支持参数传入，即，同一个模板可以给予不同的参数而达到不同的效果。  请确保OBS地址所在局点与使用RFS服务局点一致。  * vars_uri需要指向一个OBS的pre-signed URL地址，其他地址暂不支持  * 资源编排服务支持vars_body和vars_uri，如果以上两种方式中声明了同一个变量，将报错400  * vars_uri中的内容使用HCL的tfvars格式，用户可以将“.tfvars”中的内容保存到文件并上传到OBS中，并将OBS pre-signed URL传递给vars_uri  * 资源栈集不支持敏感数据加密，资源编排服务会直接明文使用、log、展示、存储vars_uri对应的参数文件内容
        :type vars_uri: str
        :param vars_body: HCL参数文件的内容。HCL模板支持参数传入，即，同一个模板可以给予不同的参数而达到不同的效果。  * vars_body使用HCL的tfvars格式，用户可以将“.tfvars”中的内容提交到vars_body中  * 资源编排服务支持vars_body和vars_uri，如果以上两种方式中声明了同一个变量，将报错400  * 如果vars_body过大，可以使用vars_uri  * 资源栈集不支持敏感数据加密，资源编排服务会直接明文使用、log、展示、存储对应的vars_body。
        :type vars_body: str
        :param use_stack_set_vars: 用户期望使用资源栈集中记录的参数值进行部署的参数名称列表。  用户只能选择已经在资源栈集中被记录的参数，如果指定了未被记录的参数会报错400。  如果use_stack_set_vars中包含资源栈实例中已经被覆盖的参数名称，则会将该参数回退至资源栈集中记录的参数值。
        :type use_stack_set_vars: list[str]
        """
        
        

        self._vars_uri = None
        self._vars_body = None
        self._use_stack_set_vars = None
        self.discriminator = None

        if vars_uri is not None:
            self.vars_uri = vars_uri
        if vars_body is not None:
            self.vars_body = vars_body
        if use_stack_set_vars is not None:
            self.use_stack_set_vars = use_stack_set_vars

    @property
    def vars_uri(self):
        r"""Gets the vars_uri of this VarOverridesPrimitiveTypeHolderVarOverrides.

        HCL参数文件的OBS地址。HCL模板支持参数传入，即，同一个模板可以给予不同的参数而达到不同的效果。  请确保OBS地址所在局点与使用RFS服务局点一致。  * vars_uri需要指向一个OBS的pre-signed URL地址，其他地址暂不支持  * 资源编排服务支持vars_body和vars_uri，如果以上两种方式中声明了同一个变量，将报错400  * vars_uri中的内容使用HCL的tfvars格式，用户可以将“.tfvars”中的内容保存到文件并上传到OBS中，并将OBS pre-signed URL传递给vars_uri  * 资源栈集不支持敏感数据加密，资源编排服务会直接明文使用、log、展示、存储vars_uri对应的参数文件内容

        :return: The vars_uri of this VarOverridesPrimitiveTypeHolderVarOverrides.
        :rtype: str
        """
        return self._vars_uri

    @vars_uri.setter
    def vars_uri(self, vars_uri):
        r"""Sets the vars_uri of this VarOverridesPrimitiveTypeHolderVarOverrides.

        HCL参数文件的OBS地址。HCL模板支持参数传入，即，同一个模板可以给予不同的参数而达到不同的效果。  请确保OBS地址所在局点与使用RFS服务局点一致。  * vars_uri需要指向一个OBS的pre-signed URL地址，其他地址暂不支持  * 资源编排服务支持vars_body和vars_uri，如果以上两种方式中声明了同一个变量，将报错400  * vars_uri中的内容使用HCL的tfvars格式，用户可以将“.tfvars”中的内容保存到文件并上传到OBS中，并将OBS pre-signed URL传递给vars_uri  * 资源栈集不支持敏感数据加密，资源编排服务会直接明文使用、log、展示、存储vars_uri对应的参数文件内容

        :param vars_uri: The vars_uri of this VarOverridesPrimitiveTypeHolderVarOverrides.
        :type vars_uri: str
        """
        self._vars_uri = vars_uri

    @property
    def vars_body(self):
        r"""Gets the vars_body of this VarOverridesPrimitiveTypeHolderVarOverrides.

        HCL参数文件的内容。HCL模板支持参数传入，即，同一个模板可以给予不同的参数而达到不同的效果。  * vars_body使用HCL的tfvars格式，用户可以将“.tfvars”中的内容提交到vars_body中  * 资源编排服务支持vars_body和vars_uri，如果以上两种方式中声明了同一个变量，将报错400  * 如果vars_body过大，可以使用vars_uri  * 资源栈集不支持敏感数据加密，资源编排服务会直接明文使用、log、展示、存储对应的vars_body。

        :return: The vars_body of this VarOverridesPrimitiveTypeHolderVarOverrides.
        :rtype: str
        """
        return self._vars_body

    @vars_body.setter
    def vars_body(self, vars_body):
        r"""Sets the vars_body of this VarOverridesPrimitiveTypeHolderVarOverrides.

        HCL参数文件的内容。HCL模板支持参数传入，即，同一个模板可以给予不同的参数而达到不同的效果。  * vars_body使用HCL的tfvars格式，用户可以将“.tfvars”中的内容提交到vars_body中  * 资源编排服务支持vars_body和vars_uri，如果以上两种方式中声明了同一个变量，将报错400  * 如果vars_body过大，可以使用vars_uri  * 资源栈集不支持敏感数据加密，资源编排服务会直接明文使用、log、展示、存储对应的vars_body。

        :param vars_body: The vars_body of this VarOverridesPrimitiveTypeHolderVarOverrides.
        :type vars_body: str
        """
        self._vars_body = vars_body

    @property
    def use_stack_set_vars(self):
        r"""Gets the use_stack_set_vars of this VarOverridesPrimitiveTypeHolderVarOverrides.

        用户期望使用资源栈集中记录的参数值进行部署的参数名称列表。  用户只能选择已经在资源栈集中被记录的参数，如果指定了未被记录的参数会报错400。  如果use_stack_set_vars中包含资源栈实例中已经被覆盖的参数名称，则会将该参数回退至资源栈集中记录的参数值。

        :return: The use_stack_set_vars of this VarOverridesPrimitiveTypeHolderVarOverrides.
        :rtype: list[str]
        """
        return self._use_stack_set_vars

    @use_stack_set_vars.setter
    def use_stack_set_vars(self, use_stack_set_vars):
        r"""Sets the use_stack_set_vars of this VarOverridesPrimitiveTypeHolderVarOverrides.

        用户期望使用资源栈集中记录的参数值进行部署的参数名称列表。  用户只能选择已经在资源栈集中被记录的参数，如果指定了未被记录的参数会报错400。  如果use_stack_set_vars中包含资源栈实例中已经被覆盖的参数名称，则会将该参数回退至资源栈集中记录的参数值。

        :param use_stack_set_vars: The use_stack_set_vars of this VarOverridesPrimitiveTypeHolderVarOverrides.
        :type use_stack_set_vars: list[str]
        """
        self._use_stack_set_vars = use_stack_set_vars

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, VarOverridesPrimitiveTypeHolderVarOverrides):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
