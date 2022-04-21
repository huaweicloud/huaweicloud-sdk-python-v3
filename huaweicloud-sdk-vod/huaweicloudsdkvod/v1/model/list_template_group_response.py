# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTemplateGroupResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'template_group_list': 'list[TemplateGroup]',
        'total': 'int',
        'error_code': 'str',
        'error_msg': 'str'
    }

    attribute_map = {
        'template_group_list': 'template_group_list',
        'total': 'total',
        'error_code': 'error_code',
        'error_msg': 'error_msg'
    }

    def __init__(self, template_group_list=None, total=None, error_code=None, error_msg=None):
        """ListTemplateGroupResponse

        The model defined in huaweicloud sdk

        :param template_group_list: 模板组信息&lt;br/&gt; 
        :type template_group_list: list[:class:`huaweicloudsdkvod.v1.TemplateGroup`]
        :param total: 总记录条数&lt;br/&gt; 
        :type total: int
        :param error_code: 错误码&lt;br/&gt; 
        :type error_code: str
        :param error_msg: 错误描述&lt;br/&gt; 
        :type error_msg: str
        """
        
        super(ListTemplateGroupResponse, self).__init__()

        self._template_group_list = None
        self._total = None
        self._error_code = None
        self._error_msg = None
        self.discriminator = None

        if template_group_list is not None:
            self.template_group_list = template_group_list
        if total is not None:
            self.total = total
        if error_code is not None:
            self.error_code = error_code
        if error_msg is not None:
            self.error_msg = error_msg

    @property
    def template_group_list(self):
        """Gets the template_group_list of this ListTemplateGroupResponse.

        模板组信息<br/> 

        :return: The template_group_list of this ListTemplateGroupResponse.
        :rtype: list[:class:`huaweicloudsdkvod.v1.TemplateGroup`]
        """
        return self._template_group_list

    @template_group_list.setter
    def template_group_list(self, template_group_list):
        """Sets the template_group_list of this ListTemplateGroupResponse.

        模板组信息<br/> 

        :param template_group_list: The template_group_list of this ListTemplateGroupResponse.
        :type template_group_list: list[:class:`huaweicloudsdkvod.v1.TemplateGroup`]
        """
        self._template_group_list = template_group_list

    @property
    def total(self):
        """Gets the total of this ListTemplateGroupResponse.

        总记录条数<br/> 

        :return: The total of this ListTemplateGroupResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListTemplateGroupResponse.

        总记录条数<br/> 

        :param total: The total of this ListTemplateGroupResponse.
        :type total: int
        """
        self._total = total

    @property
    def error_code(self):
        """Gets the error_code of this ListTemplateGroupResponse.

        错误码<br/> 

        :return: The error_code of this ListTemplateGroupResponse.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this ListTemplateGroupResponse.

        错误码<br/> 

        :param error_code: The error_code of this ListTemplateGroupResponse.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_msg(self):
        """Gets the error_msg of this ListTemplateGroupResponse.

        错误描述<br/> 

        :return: The error_msg of this ListTemplateGroupResponse.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        """Sets the error_msg of this ListTemplateGroupResponse.

        错误描述<br/> 

        :param error_msg: The error_msg of this ListTemplateGroupResponse.
        :type error_msg: str
        """
        self._error_msg = error_msg

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
        if not isinstance(other, ListTemplateGroupResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
