# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateDataSourceResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'type': 'str',
        'content': 'ContentDetailRsp',
        'created_time': 'str',
        'modified_time': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'type': 'type',
        'content': 'content',
        'created_time': 'created_time',
        'modified_time': 'modified_time'
    }

    def __init__(self, id=None, name=None, type=None, content=None, created_time=None, modified_time=None):
        """UpdateDataSourceResponse

        The model defined in huaweicloud sdk

        :param id: 数据源id
        :type id: str
        :param name: 数据源名称
        :type name: str
        :param type: 数据源类型, 包括：IOTDA、API[、OBS、DIS、SMN、FUNCTION_GRAPH、MODEL_ARTS、DCS、KAFKA](tag:IoTA-Cloud-Only)、NODE。数据源不支持修改类型。
        :type type: str
        :param content: 
        :type content: :class:`huaweicloudsdkiotanalytics.v1.ContentDetailRsp`
        :param created_time: 创建时间，格式为：yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39;
        :type created_time: str
        :param modified_time: 修改时间，格式为：yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39;
        :type modified_time: str
        """
        
        super(UpdateDataSourceResponse, self).__init__()

        self._id = None
        self._name = None
        self._type = None
        self._content = None
        self._created_time = None
        self._modified_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if content is not None:
            self.content = content
        if created_time is not None:
            self.created_time = created_time
        if modified_time is not None:
            self.modified_time = modified_time

    @property
    def id(self):
        """Gets the id of this UpdateDataSourceResponse.

        数据源id

        :return: The id of this UpdateDataSourceResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UpdateDataSourceResponse.

        数据源id

        :param id: The id of this UpdateDataSourceResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this UpdateDataSourceResponse.

        数据源名称

        :return: The name of this UpdateDataSourceResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateDataSourceResponse.

        数据源名称

        :param name: The name of this UpdateDataSourceResponse.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        """Gets the type of this UpdateDataSourceResponse.

        数据源类型, 包括：IOTDA、API[、OBS、DIS、SMN、FUNCTION_GRAPH、MODEL_ARTS、DCS、KAFKA](tag:IoTA-Cloud-Only)、NODE。数据源不支持修改类型。

        :return: The type of this UpdateDataSourceResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this UpdateDataSourceResponse.

        数据源类型, 包括：IOTDA、API[、OBS、DIS、SMN、FUNCTION_GRAPH、MODEL_ARTS、DCS、KAFKA](tag:IoTA-Cloud-Only)、NODE。数据源不支持修改类型。

        :param type: The type of this UpdateDataSourceResponse.
        :type type: str
        """
        self._type = type

    @property
    def content(self):
        """Gets the content of this UpdateDataSourceResponse.

        :return: The content of this UpdateDataSourceResponse.
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.ContentDetailRsp`
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this UpdateDataSourceResponse.

        :param content: The content of this UpdateDataSourceResponse.
        :type content: :class:`huaweicloudsdkiotanalytics.v1.ContentDetailRsp`
        """
        self._content = content

    @property
    def created_time(self):
        """Gets the created_time of this UpdateDataSourceResponse.

        创建时间，格式为：yyyy-MM-dd'T'HH:mm:ss'Z'

        :return: The created_time of this UpdateDataSourceResponse.
        :rtype: str
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this UpdateDataSourceResponse.

        创建时间，格式为：yyyy-MM-dd'T'HH:mm:ss'Z'

        :param created_time: The created_time of this UpdateDataSourceResponse.
        :type created_time: str
        """
        self._created_time = created_time

    @property
    def modified_time(self):
        """Gets the modified_time of this UpdateDataSourceResponse.

        修改时间，格式为：yyyy-MM-dd'T'HH:mm:ss'Z'

        :return: The modified_time of this UpdateDataSourceResponse.
        :rtype: str
        """
        return self._modified_time

    @modified_time.setter
    def modified_time(self, modified_time):
        """Sets the modified_time of this UpdateDataSourceResponse.

        修改时间，格式为：yyyy-MM-dd'T'HH:mm:ss'Z'

        :param modified_time: The modified_time of this UpdateDataSourceResponse.
        :type modified_time: str
        """
        self._modified_time = modified_time

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
        if not isinstance(other, UpdateDataSourceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
