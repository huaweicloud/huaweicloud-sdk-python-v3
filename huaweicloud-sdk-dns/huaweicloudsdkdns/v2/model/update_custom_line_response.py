# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateCustomLineResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'line_id': 'str',
        'name': 'str',
        'ip_segments': 'list[str]',
        'created_at': 'str',
        'updated_at': 'str',
        'status': 'str',
        'description': 'str'
    }

    attribute_map = {
        'line_id': 'line_id',
        'name': 'name',
        'ip_segments': 'ip_segments',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'status': 'status',
        'description': 'description'
    }

    def __init__(self, line_id=None, name=None, ip_segments=None, created_at=None, updated_at=None, status=None, description=None):
        """UpdateCustomLineResponse

        The model defined in huaweicloud sdk

        :param line_id: 解析线路ID。
        :type line_id: str
        :param name: 解析线路名称。
        :type name: str
        :param ip_segments: IP地址段。
        :type ip_segments: list[str]
        :param created_at: 创建时间。
        :type created_at: str
        :param updated_at: 更新时间。
        :type updated_at: str
        :param status: 资源状态。
        :type status: str
        :param description: 自定义线路的描述信息。
        :type description: str
        """
        
        super(UpdateCustomLineResponse, self).__init__()

        self._line_id = None
        self._name = None
        self._ip_segments = None
        self._created_at = None
        self._updated_at = None
        self._status = None
        self._description = None
        self.discriminator = None

        if line_id is not None:
            self.line_id = line_id
        if name is not None:
            self.name = name
        if ip_segments is not None:
            self.ip_segments = ip_segments
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if status is not None:
            self.status = status
        if description is not None:
            self.description = description

    @property
    def line_id(self):
        """Gets the line_id of this UpdateCustomLineResponse.

        解析线路ID。

        :return: The line_id of this UpdateCustomLineResponse.
        :rtype: str
        """
        return self._line_id

    @line_id.setter
    def line_id(self, line_id):
        """Sets the line_id of this UpdateCustomLineResponse.

        解析线路ID。

        :param line_id: The line_id of this UpdateCustomLineResponse.
        :type line_id: str
        """
        self._line_id = line_id

    @property
    def name(self):
        """Gets the name of this UpdateCustomLineResponse.

        解析线路名称。

        :return: The name of this UpdateCustomLineResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateCustomLineResponse.

        解析线路名称。

        :param name: The name of this UpdateCustomLineResponse.
        :type name: str
        """
        self._name = name

    @property
    def ip_segments(self):
        """Gets the ip_segments of this UpdateCustomLineResponse.

        IP地址段。

        :return: The ip_segments of this UpdateCustomLineResponse.
        :rtype: list[str]
        """
        return self._ip_segments

    @ip_segments.setter
    def ip_segments(self, ip_segments):
        """Sets the ip_segments of this UpdateCustomLineResponse.

        IP地址段。

        :param ip_segments: The ip_segments of this UpdateCustomLineResponse.
        :type ip_segments: list[str]
        """
        self._ip_segments = ip_segments

    @property
    def created_at(self):
        """Gets the created_at of this UpdateCustomLineResponse.

        创建时间。

        :return: The created_at of this UpdateCustomLineResponse.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this UpdateCustomLineResponse.

        创建时间。

        :param created_at: The created_at of this UpdateCustomLineResponse.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this UpdateCustomLineResponse.

        更新时间。

        :return: The updated_at of this UpdateCustomLineResponse.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this UpdateCustomLineResponse.

        更新时间。

        :param updated_at: The updated_at of this UpdateCustomLineResponse.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def status(self):
        """Gets the status of this UpdateCustomLineResponse.

        资源状态。

        :return: The status of this UpdateCustomLineResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UpdateCustomLineResponse.

        资源状态。

        :param status: The status of this UpdateCustomLineResponse.
        :type status: str
        """
        self._status = status

    @property
    def description(self):
        """Gets the description of this UpdateCustomLineResponse.

        自定义线路的描述信息。

        :return: The description of this UpdateCustomLineResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateCustomLineResponse.

        自定义线路的描述信息。

        :param description: The description of this UpdateCustomLineResponse.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, UpdateCustomLineResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
