# coding: utf-8

import re
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
        'ief_instance_id': 'str',
        'app_id': 'str',
        'limit': 'str',
        'offset': 'str'
    }

    attribute_map = {
        'ief_instance_id': 'ief-instance-id',
        'app_id': 'app_id',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, ief_instance_id=None, app_id=None, limit=None, offset=None):
        """ListAppVersionsRequest

        The model defined in huaweicloud sdk

        :param ief_instance_id: 铂金版实例ID，专业版实例为空值
        :type ief_instance_id: str
        :param app_id: 应用模板ID
        :type app_id: str
        :param limit: 每页显示的条目数量，取值范围1~1000，默认为1000
        :type limit: str
        :param offset: 查询的起始位置，取值范围为非负整数，默认为0
        :type offset: str
        """
        
        

        self._ief_instance_id = None
        self._app_id = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        if ief_instance_id is not None:
            self.ief_instance_id = ief_instance_id
        self.app_id = app_id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def ief_instance_id(self):
        """Gets the ief_instance_id of this ListAppVersionsRequest.

        铂金版实例ID，专业版实例为空值

        :return: The ief_instance_id of this ListAppVersionsRequest.
        :rtype: str
        """
        return self._ief_instance_id

    @ief_instance_id.setter
    def ief_instance_id(self, ief_instance_id):
        """Sets the ief_instance_id of this ListAppVersionsRequest.

        铂金版实例ID，专业版实例为空值

        :param ief_instance_id: The ief_instance_id of this ListAppVersionsRequest.
        :type ief_instance_id: str
        """
        self._ief_instance_id = ief_instance_id

    @property
    def app_id(self):
        """Gets the app_id of this ListAppVersionsRequest.

        应用模板ID

        :return: The app_id of this ListAppVersionsRequest.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this ListAppVersionsRequest.

        应用模板ID

        :param app_id: The app_id of this ListAppVersionsRequest.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def limit(self):
        """Gets the limit of this ListAppVersionsRequest.

        每页显示的条目数量，取值范围1~1000，默认为1000

        :return: The limit of this ListAppVersionsRequest.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListAppVersionsRequest.

        每页显示的条目数量，取值范围1~1000，默认为1000

        :param limit: The limit of this ListAppVersionsRequest.
        :type limit: str
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListAppVersionsRequest.

        查询的起始位置，取值范围为非负整数，默认为0

        :return: The offset of this ListAppVersionsRequest.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListAppVersionsRequest.

        查询的起始位置，取值范围为非负整数，默认为0

        :param offset: The offset of this ListAppVersionsRequest.
        :type offset: str
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
