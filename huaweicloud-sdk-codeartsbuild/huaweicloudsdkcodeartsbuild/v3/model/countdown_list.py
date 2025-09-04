# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CountdownList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'service_type': 'str',
        'resource_id': 'str',
        'resource_name': 'str',
        'resource_type': 'str',
        'resource_spec_code': 'str',
        'tips': 'CountdownListTips'
    }

    attribute_map = {
        'service_type': 'service_type',
        'resource_id': 'resource_id',
        'resource_name': 'resource_name',
        'resource_type': 'resource_type',
        'resource_spec_code': 'resource_spec_code',
        'tips': 'tips'
    }

    def __init__(self, service_type=None, resource_id=None, resource_name=None, resource_type=None, resource_spec_code=None, tips=None):
        r"""CountdownList

        The model defined in huaweicloud sdk

        :param service_type: 服务类型
        :type service_type: str
        :param resource_id: 资源编号
        :type resource_id: str
        :param resource_name: 资源名称
        :type resource_name: str
        :param resource_type: 资源类型
        :type resource_type: str
        :param resource_spec_code: 资源规格
        :type resource_spec_code: str
        :param tips: 
        :type tips: :class:`huaweicloudsdkcodeartsbuild.v3.CountdownListTips`
        """
        
        

        self._service_type = None
        self._resource_id = None
        self._resource_name = None
        self._resource_type = None
        self._resource_spec_code = None
        self._tips = None
        self.discriminator = None

        if service_type is not None:
            self.service_type = service_type
        if resource_id is not None:
            self.resource_id = resource_id
        if resource_name is not None:
            self.resource_name = resource_name
        if resource_type is not None:
            self.resource_type = resource_type
        if resource_spec_code is not None:
            self.resource_spec_code = resource_spec_code
        if tips is not None:
            self.tips = tips

    @property
    def service_type(self):
        r"""Gets the service_type of this CountdownList.

        服务类型

        :return: The service_type of this CountdownList.
        :rtype: str
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        r"""Sets the service_type of this CountdownList.

        服务类型

        :param service_type: The service_type of this CountdownList.
        :type service_type: str
        """
        self._service_type = service_type

    @property
    def resource_id(self):
        r"""Gets the resource_id of this CountdownList.

        资源编号

        :return: The resource_id of this CountdownList.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this CountdownList.

        资源编号

        :param resource_id: The resource_id of this CountdownList.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def resource_name(self):
        r"""Gets the resource_name of this CountdownList.

        资源名称

        :return: The resource_name of this CountdownList.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        r"""Sets the resource_name of this CountdownList.

        资源名称

        :param resource_name: The resource_name of this CountdownList.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def resource_type(self):
        r"""Gets the resource_type of this CountdownList.

        资源类型

        :return: The resource_type of this CountdownList.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this CountdownList.

        资源类型

        :param resource_type: The resource_type of this CountdownList.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def resource_spec_code(self):
        r"""Gets the resource_spec_code of this CountdownList.

        资源规格

        :return: The resource_spec_code of this CountdownList.
        :rtype: str
        """
        return self._resource_spec_code

    @resource_spec_code.setter
    def resource_spec_code(self, resource_spec_code):
        r"""Sets the resource_spec_code of this CountdownList.

        资源规格

        :param resource_spec_code: The resource_spec_code of this CountdownList.
        :type resource_spec_code: str
        """
        self._resource_spec_code = resource_spec_code

    @property
    def tips(self):
        r"""Gets the tips of this CountdownList.

        :return: The tips of this CountdownList.
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.CountdownListTips`
        """
        return self._tips

    @tips.setter
    def tips(self, tips):
        r"""Sets the tips of this CountdownList.

        :param tips: The tips of this CountdownList.
        :type tips: :class:`huaweicloudsdkcodeartsbuild.v3.CountdownListTips`
        """
        self._tips = tips

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
        if not isinstance(other, CountdownList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
