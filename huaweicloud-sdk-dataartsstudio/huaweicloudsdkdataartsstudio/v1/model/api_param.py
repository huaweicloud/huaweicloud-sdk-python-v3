# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApiParam:

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
        'create_user': 'str',
        'description': 'str',
        'tags': 'list[str]',
        'table_name': 'str',
        'publish_status_type': 'str',
        'api_specific_type_str': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'authorization_status_type': 'str'
    }

    attribute_map = {
        'name': 'name',
        'create_user': 'create_user',
        'description': 'description',
        'tags': 'tags',
        'table_name': 'table_name',
        'publish_status_type': 'publish_status_type',
        'api_specific_type_str': 'api_specific_type_str',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'authorization_status_type': 'authorization_status_type'
    }

    def __init__(self, name=None, create_user=None, description=None, tags=None, table_name=None, publish_status_type=None, api_specific_type_str=None, start_time=None, end_time=None, authorization_status_type=None):
        r"""ApiParam

        The model defined in huaweicloud sdk

        :param name: API名称。
        :type name: str
        :param create_user: API创建人名称。
        :type create_user: str
        :param description: API描述。
        :type description: str
        :param tags: API标签列表。
        :type tags: list[str]
        :param table_name: API所使用到的数据库表名。
        :type table_name: str
        :param publish_status_type: API发布状态。
        :type publish_status_type: str
        :param api_specific_type_str: API取数方式。
        :type api_specific_type_str: str
        :param start_time: API创建开始时间。
        :type start_time: str
        :param end_time: API创建结束时间。
        :type end_time: str
        :param authorization_status_type: 
        :type authorization_status_type: str
        """
        
        

        self._name = None
        self._create_user = None
        self._description = None
        self._tags = None
        self._table_name = None
        self._publish_status_type = None
        self._api_specific_type_str = None
        self._start_time = None
        self._end_time = None
        self._authorization_status_type = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if create_user is not None:
            self.create_user = create_user
        if description is not None:
            self.description = description
        if tags is not None:
            self.tags = tags
        if table_name is not None:
            self.table_name = table_name
        if publish_status_type is not None:
            self.publish_status_type = publish_status_type
        if api_specific_type_str is not None:
            self.api_specific_type_str = api_specific_type_str
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if authorization_status_type is not None:
            self.authorization_status_type = authorization_status_type

    @property
    def name(self):
        r"""Gets the name of this ApiParam.

        API名称。

        :return: The name of this ApiParam.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ApiParam.

        API名称。

        :param name: The name of this ApiParam.
        :type name: str
        """
        self._name = name

    @property
    def create_user(self):
        r"""Gets the create_user of this ApiParam.

        API创建人名称。

        :return: The create_user of this ApiParam.
        :rtype: str
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        r"""Sets the create_user of this ApiParam.

        API创建人名称。

        :param create_user: The create_user of this ApiParam.
        :type create_user: str
        """
        self._create_user = create_user

    @property
    def description(self):
        r"""Gets the description of this ApiParam.

        API描述。

        :return: The description of this ApiParam.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ApiParam.

        API描述。

        :param description: The description of this ApiParam.
        :type description: str
        """
        self._description = description

    @property
    def tags(self):
        r"""Gets the tags of this ApiParam.

        API标签列表。

        :return: The tags of this ApiParam.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ApiParam.

        API标签列表。

        :param tags: The tags of this ApiParam.
        :type tags: list[str]
        """
        self._tags = tags

    @property
    def table_name(self):
        r"""Gets the table_name of this ApiParam.

        API所使用到的数据库表名。

        :return: The table_name of this ApiParam.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        r"""Sets the table_name of this ApiParam.

        API所使用到的数据库表名。

        :param table_name: The table_name of this ApiParam.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def publish_status_type(self):
        r"""Gets the publish_status_type of this ApiParam.

        API发布状态。

        :return: The publish_status_type of this ApiParam.
        :rtype: str
        """
        return self._publish_status_type

    @publish_status_type.setter
    def publish_status_type(self, publish_status_type):
        r"""Sets the publish_status_type of this ApiParam.

        API发布状态。

        :param publish_status_type: The publish_status_type of this ApiParam.
        :type publish_status_type: str
        """
        self._publish_status_type = publish_status_type

    @property
    def api_specific_type_str(self):
        r"""Gets the api_specific_type_str of this ApiParam.

        API取数方式。

        :return: The api_specific_type_str of this ApiParam.
        :rtype: str
        """
        return self._api_specific_type_str

    @api_specific_type_str.setter
    def api_specific_type_str(self, api_specific_type_str):
        r"""Sets the api_specific_type_str of this ApiParam.

        API取数方式。

        :param api_specific_type_str: The api_specific_type_str of this ApiParam.
        :type api_specific_type_str: str
        """
        self._api_specific_type_str = api_specific_type_str

    @property
    def start_time(self):
        r"""Gets the start_time of this ApiParam.

        API创建开始时间。

        :return: The start_time of this ApiParam.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ApiParam.

        API创建开始时间。

        :param start_time: The start_time of this ApiParam.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ApiParam.

        API创建结束时间。

        :return: The end_time of this ApiParam.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ApiParam.

        API创建结束时间。

        :param end_time: The end_time of this ApiParam.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def authorization_status_type(self):
        r"""Gets the authorization_status_type of this ApiParam.

        :return: The authorization_status_type of this ApiParam.
        :rtype: str
        """
        return self._authorization_status_type

    @authorization_status_type.setter
    def authorization_status_type(self, authorization_status_type):
        r"""Sets the authorization_status_type of this ApiParam.

        :param authorization_status_type: The authorization_status_type of this ApiParam.
        :type authorization_status_type: str
        """
        self._authorization_status_type = authorization_status_type

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
        if not isinstance(other, ApiParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
