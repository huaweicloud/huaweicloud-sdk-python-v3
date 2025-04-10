# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListMqsInstanceTopicsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'app_name': 'str',
        'name': 'str',
        'access_policy': 'str',
        'limit': 'str',
        'offset': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'app_name': 'app_name',
        'name': 'name',
        'access_policy': 'access_policy',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, instance_id=None, app_name=None, name=None, access_policy=None, limit=None, offset=None):
        r"""ListMqsInstanceTopicsRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID。
        :type instance_id: str
        :param app_name: 应用名称。
        :type app_name: str
        :param name: Topic名称。
        :type name: str
        :param access_policy: 权限类型。 - all：发布+订阅 - pub：发布 - sub：订阅
        :type access_policy: str
        :param limit: 分页查询大小。默认查询所有的topic。
        :type limit: str
        :param offset: 分页查询的偏移量。默认值是0。
        :type offset: str
        """
        
        

        self._instance_id = None
        self._app_name = None
        self._name = None
        self._access_policy = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        self.instance_id = instance_id
        if app_name is not None:
            self.app_name = app_name
        if name is not None:
            self.name = name
        if access_policy is not None:
            self.access_policy = access_policy
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListMqsInstanceTopicsRequest.

        实例ID。

        :return: The instance_id of this ListMqsInstanceTopicsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListMqsInstanceTopicsRequest.

        实例ID。

        :param instance_id: The instance_id of this ListMqsInstanceTopicsRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def app_name(self):
        r"""Gets the app_name of this ListMqsInstanceTopicsRequest.

        应用名称。

        :return: The app_name of this ListMqsInstanceTopicsRequest.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        r"""Sets the app_name of this ListMqsInstanceTopicsRequest.

        应用名称。

        :param app_name: The app_name of this ListMqsInstanceTopicsRequest.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def name(self):
        r"""Gets the name of this ListMqsInstanceTopicsRequest.

        Topic名称。

        :return: The name of this ListMqsInstanceTopicsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListMqsInstanceTopicsRequest.

        Topic名称。

        :param name: The name of this ListMqsInstanceTopicsRequest.
        :type name: str
        """
        self._name = name

    @property
    def access_policy(self):
        r"""Gets the access_policy of this ListMqsInstanceTopicsRequest.

        权限类型。 - all：发布+订阅 - pub：发布 - sub：订阅

        :return: The access_policy of this ListMqsInstanceTopicsRequest.
        :rtype: str
        """
        return self._access_policy

    @access_policy.setter
    def access_policy(self, access_policy):
        r"""Sets the access_policy of this ListMqsInstanceTopicsRequest.

        权限类型。 - all：发布+订阅 - pub：发布 - sub：订阅

        :param access_policy: The access_policy of this ListMqsInstanceTopicsRequest.
        :type access_policy: str
        """
        self._access_policy = access_policy

    @property
    def limit(self):
        r"""Gets the limit of this ListMqsInstanceTopicsRequest.

        分页查询大小。默认查询所有的topic。

        :return: The limit of this ListMqsInstanceTopicsRequest.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListMqsInstanceTopicsRequest.

        分页查询大小。默认查询所有的topic。

        :param limit: The limit of this ListMqsInstanceTopicsRequest.
        :type limit: str
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListMqsInstanceTopicsRequest.

        分页查询的偏移量。默认值是0。

        :return: The offset of this ListMqsInstanceTopicsRequest.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListMqsInstanceTopicsRequest.

        分页查询的偏移量。默认值是0。

        :param offset: The offset of this ListMqsInstanceTopicsRequest.
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
        if not isinstance(other, ListMqsInstanceTopicsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
