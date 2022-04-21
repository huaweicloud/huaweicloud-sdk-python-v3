# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateProductTemplateRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'description': 'str',
        'status': 'int'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'status': 'status'
    }

    def __init__(self, name=None, description=None, status=None):
        """UpdateProductTemplateRequestBody

        The model defined in huaweicloud sdk

        :param name: 产品模板名称，支持中文,英文大小写，数字，下划线和中划线,长度2-64
        :type name: str
        :param description: 产品模板描述，长度0-200
        :type description: str
        :param status: 产品模板状态 0-启用 1-禁用
        :type status: int
        """
        
        

        self._name = None
        self._description = None
        self._status = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.status = status

    @property
    def name(self):
        """Gets the name of this UpdateProductTemplateRequestBody.

        产品模板名称，支持中文,英文大小写，数字，下划线和中划线,长度2-64

        :return: The name of this UpdateProductTemplateRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateProductTemplateRequestBody.

        产品模板名称，支持中文,英文大小写，数字，下划线和中划线,长度2-64

        :param name: The name of this UpdateProductTemplateRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this UpdateProductTemplateRequestBody.

        产品模板描述，长度0-200

        :return: The description of this UpdateProductTemplateRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateProductTemplateRequestBody.

        产品模板描述，长度0-200

        :param description: The description of this UpdateProductTemplateRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def status(self):
        """Gets the status of this UpdateProductTemplateRequestBody.

        产品模板状态 0-启用 1-禁用

        :return: The status of this UpdateProductTemplateRequestBody.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UpdateProductTemplateRequestBody.

        产品模板状态 0-启用 1-禁用

        :param status: The status of this UpdateProductTemplateRequestBody.
        :type status: int
        """
        self._status = status

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
        if not isinstance(other, UpdateProductTemplateRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
