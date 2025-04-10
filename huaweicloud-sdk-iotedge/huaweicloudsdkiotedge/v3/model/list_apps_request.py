# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAppsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'app_type': 'str',
        'provider_type': 'str',
        'app_id': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'app_type': 'app_type',
        'provider_type': 'provider_type',
        'app_id': 'app_id',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, app_type=None, provider_type=None, app_id=None, limit=None, offset=None):
        r"""ListAppsRequest

        The model defined in huaweicloud sdk

        :param app_type: 应用类型
        :type app_type: str
        :param provider_type: 应用来源
        :type provider_type: str
        :param app_id: 应用ID
        :type app_id: str
        :param limit: 每页记录数，默认值为10，取值区间为1-1000。
        :type limit: int
        :param offset: 查询的起始位置，取值范围为非负整数，默认为0。
        :type offset: int
        """
        
        

        self._app_type = None
        self._provider_type = None
        self._app_id = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        if app_type is not None:
            self.app_type = app_type
        if provider_type is not None:
            self.provider_type = provider_type
        if app_id is not None:
            self.app_id = app_id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def app_type(self):
        r"""Gets the app_type of this ListAppsRequest.

        应用类型

        :return: The app_type of this ListAppsRequest.
        :rtype: str
        """
        return self._app_type

    @app_type.setter
    def app_type(self, app_type):
        r"""Sets the app_type of this ListAppsRequest.

        应用类型

        :param app_type: The app_type of this ListAppsRequest.
        :type app_type: str
        """
        self._app_type = app_type

    @property
    def provider_type(self):
        r"""Gets the provider_type of this ListAppsRequest.

        应用来源

        :return: The provider_type of this ListAppsRequest.
        :rtype: str
        """
        return self._provider_type

    @provider_type.setter
    def provider_type(self, provider_type):
        r"""Sets the provider_type of this ListAppsRequest.

        应用来源

        :param provider_type: The provider_type of this ListAppsRequest.
        :type provider_type: str
        """
        self._provider_type = provider_type

    @property
    def app_id(self):
        r"""Gets the app_id of this ListAppsRequest.

        应用ID

        :return: The app_id of this ListAppsRequest.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        r"""Sets the app_id of this ListAppsRequest.

        应用ID

        :param app_id: The app_id of this ListAppsRequest.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def limit(self):
        r"""Gets the limit of this ListAppsRequest.

        每页记录数，默认值为10，取值区间为1-1000。

        :return: The limit of this ListAppsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListAppsRequest.

        每页记录数，默认值为10，取值区间为1-1000。

        :param limit: The limit of this ListAppsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListAppsRequest.

        查询的起始位置，取值范围为非负整数，默认为0。

        :return: The offset of this ListAppsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListAppsRequest.

        查询的起始位置，取值范围为非负整数，默认为0。

        :param offset: The offset of this ListAppsRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ListAppsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
