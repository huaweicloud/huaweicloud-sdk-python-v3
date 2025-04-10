# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateBasicAwReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'body_param_type': 'str',
        'description': 'str',
        'dft_check_point_list': 'list[CheckPoint]',
        'dft_custom_header': 'list[AwParam]',
        'dft_variable_list': 'list[AwVariable]',
        'extra_info': 'ExtraInfo',
        'group_name': 'str',
        'name': 'str',
        'param_type_and_dft_value': 'list[AwParam]'
    }

    attribute_map = {
        'body_param_type': 'body_param_type',
        'description': 'description',
        'dft_check_point_list': 'dft_check_point_list',
        'dft_custom_header': 'dft_custom_header',
        'dft_variable_list': 'dft_variable_list',
        'extra_info': 'extra_info',
        'group_name': 'group_name',
        'name': 'name',
        'param_type_and_dft_value': 'param_type_and_dft_value'
    }

    def __init__(self, body_param_type=None, description=None, dft_check_point_list=None, dft_custom_header=None, dft_variable_list=None, extra_info=None, group_name=None, name=None, param_type_and_dft_value=None):
        r"""CreateBasicAwReq

        The model defined in huaweicloud sdk

        :param body_param_type: body请求体的类型：text(包含JSON，参数内部区分)、form
        :type body_param_type: str
        :param description: 描述
        :type description: str
        :param dft_check_point_list: 默认检查点List
        :type dft_check_point_list: list[:class:`huaweicloudsdkcloudtest.v1.CheckPoint`]
        :param dft_custom_header: 默认请求头参数对象
        :type dft_custom_header: list[:class:`huaweicloudsdkcloudtest.v1.AwParam`]
        :param dft_variable_list: 定义的变量信息
        :type dft_variable_list: list[:class:`huaweicloudsdkcloudtest.v1.AwVariable`]
        :param extra_info: 
        :type extra_info: :class:`huaweicloudsdkcloudtest.v1.ExtraInfo`
        :param group_name: 组名
        :type group_name: str
        :param name: 名称
        :type name: str
        :param param_type_and_dft_value: 参数类型和参数默认值对应List
        :type param_type_and_dft_value: list[:class:`huaweicloudsdkcloudtest.v1.AwParam`]
        """
        
        

        self._body_param_type = None
        self._description = None
        self._dft_check_point_list = None
        self._dft_custom_header = None
        self._dft_variable_list = None
        self._extra_info = None
        self._group_name = None
        self._name = None
        self._param_type_and_dft_value = None
        self.discriminator = None

        if body_param_type is not None:
            self.body_param_type = body_param_type
        if description is not None:
            self.description = description
        if dft_check_point_list is not None:
            self.dft_check_point_list = dft_check_point_list
        if dft_custom_header is not None:
            self.dft_custom_header = dft_custom_header
        if dft_variable_list is not None:
            self.dft_variable_list = dft_variable_list
        if extra_info is not None:
            self.extra_info = extra_info
        if group_name is not None:
            self.group_name = group_name
        if name is not None:
            self.name = name
        if param_type_and_dft_value is not None:
            self.param_type_and_dft_value = param_type_and_dft_value

    @property
    def body_param_type(self):
        r"""Gets the body_param_type of this CreateBasicAwReq.

        body请求体的类型：text(包含JSON，参数内部区分)、form

        :return: The body_param_type of this CreateBasicAwReq.
        :rtype: str
        """
        return self._body_param_type

    @body_param_type.setter
    def body_param_type(self, body_param_type):
        r"""Sets the body_param_type of this CreateBasicAwReq.

        body请求体的类型：text(包含JSON，参数内部区分)、form

        :param body_param_type: The body_param_type of this CreateBasicAwReq.
        :type body_param_type: str
        """
        self._body_param_type = body_param_type

    @property
    def description(self):
        r"""Gets the description of this CreateBasicAwReq.

        描述

        :return: The description of this CreateBasicAwReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateBasicAwReq.

        描述

        :param description: The description of this CreateBasicAwReq.
        :type description: str
        """
        self._description = description

    @property
    def dft_check_point_list(self):
        r"""Gets the dft_check_point_list of this CreateBasicAwReq.

        默认检查点List

        :return: The dft_check_point_list of this CreateBasicAwReq.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.CheckPoint`]
        """
        return self._dft_check_point_list

    @dft_check_point_list.setter
    def dft_check_point_list(self, dft_check_point_list):
        r"""Sets the dft_check_point_list of this CreateBasicAwReq.

        默认检查点List

        :param dft_check_point_list: The dft_check_point_list of this CreateBasicAwReq.
        :type dft_check_point_list: list[:class:`huaweicloudsdkcloudtest.v1.CheckPoint`]
        """
        self._dft_check_point_list = dft_check_point_list

    @property
    def dft_custom_header(self):
        r"""Gets the dft_custom_header of this CreateBasicAwReq.

        默认请求头参数对象

        :return: The dft_custom_header of this CreateBasicAwReq.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.AwParam`]
        """
        return self._dft_custom_header

    @dft_custom_header.setter
    def dft_custom_header(self, dft_custom_header):
        r"""Sets the dft_custom_header of this CreateBasicAwReq.

        默认请求头参数对象

        :param dft_custom_header: The dft_custom_header of this CreateBasicAwReq.
        :type dft_custom_header: list[:class:`huaweicloudsdkcloudtest.v1.AwParam`]
        """
        self._dft_custom_header = dft_custom_header

    @property
    def dft_variable_list(self):
        r"""Gets the dft_variable_list of this CreateBasicAwReq.

        定义的变量信息

        :return: The dft_variable_list of this CreateBasicAwReq.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.AwVariable`]
        """
        return self._dft_variable_list

    @dft_variable_list.setter
    def dft_variable_list(self, dft_variable_list):
        r"""Sets the dft_variable_list of this CreateBasicAwReq.

        定义的变量信息

        :param dft_variable_list: The dft_variable_list of this CreateBasicAwReq.
        :type dft_variable_list: list[:class:`huaweicloudsdkcloudtest.v1.AwVariable`]
        """
        self._dft_variable_list = dft_variable_list

    @property
    def extra_info(self):
        r"""Gets the extra_info of this CreateBasicAwReq.

        :return: The extra_info of this CreateBasicAwReq.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.ExtraInfo`
        """
        return self._extra_info

    @extra_info.setter
    def extra_info(self, extra_info):
        r"""Sets the extra_info of this CreateBasicAwReq.

        :param extra_info: The extra_info of this CreateBasicAwReq.
        :type extra_info: :class:`huaweicloudsdkcloudtest.v1.ExtraInfo`
        """
        self._extra_info = extra_info

    @property
    def group_name(self):
        r"""Gets the group_name of this CreateBasicAwReq.

        组名

        :return: The group_name of this CreateBasicAwReq.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        r"""Sets the group_name of this CreateBasicAwReq.

        组名

        :param group_name: The group_name of this CreateBasicAwReq.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def name(self):
        r"""Gets the name of this CreateBasicAwReq.

        名称

        :return: The name of this CreateBasicAwReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateBasicAwReq.

        名称

        :param name: The name of this CreateBasicAwReq.
        :type name: str
        """
        self._name = name

    @property
    def param_type_and_dft_value(self):
        r"""Gets the param_type_and_dft_value of this CreateBasicAwReq.

        参数类型和参数默认值对应List

        :return: The param_type_and_dft_value of this CreateBasicAwReq.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.AwParam`]
        """
        return self._param_type_and_dft_value

    @param_type_and_dft_value.setter
    def param_type_and_dft_value(self, param_type_and_dft_value):
        r"""Sets the param_type_and_dft_value of this CreateBasicAwReq.

        参数类型和参数默认值对应List

        :param param_type_and_dft_value: The param_type_and_dft_value of this CreateBasicAwReq.
        :type param_type_and_dft_value: list[:class:`huaweicloudsdkcloudtest.v1.AwParam`]
        """
        self._param_type_and_dft_value = param_type_and_dft_value

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
        if not isinstance(other, CreateBasicAwReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
