# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListComponentsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_environment_id': 'str',
        'x_enterprise_project_id': 'str',
        'limit': 'str',
        'offset': 'str',
        'application_id': 'str'
    }

    attribute_map = {
        'x_environment_id': 'X-Environment-ID',
        'x_enterprise_project_id': 'X-Enterprise-Project-ID',
        'limit': 'limit',
        'offset': 'offset',
        'application_id': 'application_id'
    }

    def __init__(self, x_environment_id=None, x_enterprise_project_id=None, limit=None, offset=None, application_id=None):
        """ListComponentsRequest

        The model defined in huaweicloud sdk

        :param x_environment_id: 环境id。
        :type x_environment_id: str
        :param x_enterprise_project_id: 租户的企业项目id。
        :type x_enterprise_project_id: str
        :param limit: 限制本次返回结果的条数。
        :type limit: str
        :param offset: 分页偏移位，查询起始位置。
        :type offset: str
        :param application_id: 应用id。
        :type application_id: str
        """
        
        

        self._x_environment_id = None
        self._x_enterprise_project_id = None
        self._limit = None
        self._offset = None
        self._application_id = None
        self.discriminator = None

        self.x_environment_id = x_environment_id
        if x_enterprise_project_id is not None:
            self.x_enterprise_project_id = x_enterprise_project_id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        self.application_id = application_id

    @property
    def x_environment_id(self):
        """Gets the x_environment_id of this ListComponentsRequest.

        环境id。

        :return: The x_environment_id of this ListComponentsRequest.
        :rtype: str
        """
        return self._x_environment_id

    @x_environment_id.setter
    def x_environment_id(self, x_environment_id):
        """Sets the x_environment_id of this ListComponentsRequest.

        环境id。

        :param x_environment_id: The x_environment_id of this ListComponentsRequest.
        :type x_environment_id: str
        """
        self._x_environment_id = x_environment_id

    @property
    def x_enterprise_project_id(self):
        """Gets the x_enterprise_project_id of this ListComponentsRequest.

        租户的企业项目id。

        :return: The x_enterprise_project_id of this ListComponentsRequest.
        :rtype: str
        """
        return self._x_enterprise_project_id

    @x_enterprise_project_id.setter
    def x_enterprise_project_id(self, x_enterprise_project_id):
        """Sets the x_enterprise_project_id of this ListComponentsRequest.

        租户的企业项目id。

        :param x_enterprise_project_id: The x_enterprise_project_id of this ListComponentsRequest.
        :type x_enterprise_project_id: str
        """
        self._x_enterprise_project_id = x_enterprise_project_id

    @property
    def limit(self):
        """Gets the limit of this ListComponentsRequest.

        限制本次返回结果的条数。

        :return: The limit of this ListComponentsRequest.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListComponentsRequest.

        限制本次返回结果的条数。

        :param limit: The limit of this ListComponentsRequest.
        :type limit: str
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListComponentsRequest.

        分页偏移位，查询起始位置。

        :return: The offset of this ListComponentsRequest.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListComponentsRequest.

        分页偏移位，查询起始位置。

        :param offset: The offset of this ListComponentsRequest.
        :type offset: str
        """
        self._offset = offset

    @property
    def application_id(self):
        """Gets the application_id of this ListComponentsRequest.

        应用id。

        :return: The application_id of this ListComponentsRequest.
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        """Sets the application_id of this ListComponentsRequest.

        应用id。

        :param application_id: The application_id of this ListComponentsRequest.
        :type application_id: str
        """
        self._application_id = application_id

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
        if not isinstance(other, ListComponentsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
