# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAppVersionsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'app_id': 'str',
        'version': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'app_id': 'app_id',
        'version': 'version',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, app_id=None, version=None, limit=None, offset=None):
        r"""ListAppVersionsRequest

        The model defined in huaweicloud sdk

        :param app_id: 应用ID
        :type app_id: str
        :param version: 应用版本号
        :type version: str
        :param limit: 每页记录数，默认值为10，取值区间为1-1000。
        :type limit: int
        :param offset: 查询的起始位置，取值范围为非负整数，默认为0。
        :type offset: int
        """
        
        

        self._app_id = None
        self._version = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        self.app_id = app_id
        if version is not None:
            self.version = version
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def app_id(self):
        r"""Gets the app_id of this ListAppVersionsRequest.

        应用ID

        :return: The app_id of this ListAppVersionsRequest.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        r"""Sets the app_id of this ListAppVersionsRequest.

        应用ID

        :param app_id: The app_id of this ListAppVersionsRequest.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def version(self):
        r"""Gets the version of this ListAppVersionsRequest.

        应用版本号

        :return: The version of this ListAppVersionsRequest.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this ListAppVersionsRequest.

        应用版本号

        :param version: The version of this ListAppVersionsRequest.
        :type version: str
        """
        self._version = version

    @property
    def limit(self):
        r"""Gets the limit of this ListAppVersionsRequest.

        每页记录数，默认值为10，取值区间为1-1000。

        :return: The limit of this ListAppVersionsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListAppVersionsRequest.

        每页记录数，默认值为10，取值区间为1-1000。

        :param limit: The limit of this ListAppVersionsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListAppVersionsRequest.

        查询的起始位置，取值范围为非负整数，默认为0。

        :return: The offset of this ListAppVersionsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListAppVersionsRequest.

        查询的起始位置，取值范围为非负整数，默认为0。

        :param offset: The offset of this ListAppVersionsRequest.
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
        if not isinstance(other, ListAppVersionsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
