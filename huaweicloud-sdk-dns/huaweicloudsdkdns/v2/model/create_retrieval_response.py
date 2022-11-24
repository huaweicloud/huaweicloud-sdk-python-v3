# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateRetrievalResponse(SdkResponse):

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
        'zone_name': 'str',
        'record': 'CreatePublicZoneFindRespRecord',
        'status': 'str',
        'created_at': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'id': 'id',
        'zone_name': 'zone_name',
        'record': 'record',
        'status': 'status',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, zone_name=None, record=None, status=None, created_at=None, updated_at=None):
        """CreateRetrievalResponse

        The model defined in huaweicloud sdk

        :param id: 找回请求ID。
        :type id: str
        :param zone_name: 域名名称。
        :type zone_name: str
        :param record: 
        :type record: :class:`huaweicloudsdkdns.v2.CreatePublicZoneFindRespRecord`
        :param status: 状态，(PENDING,VERIFIED,CREATED,EXPIRED)
        :type status: str
        :param created_at: 创建时间。
        :type created_at: str
        :param updated_at: 更新时间。
        :type updated_at: str
        """
        
        super(CreateRetrievalResponse, self).__init__()

        self._id = None
        self._zone_name = None
        self._record = None
        self._status = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if zone_name is not None:
            self.zone_name = zone_name
        if record is not None:
            self.record = record
        if status is not None:
            self.status = status
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this CreateRetrievalResponse.

        找回请求ID。

        :return: The id of this CreateRetrievalResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreateRetrievalResponse.

        找回请求ID。

        :param id: The id of this CreateRetrievalResponse.
        :type id: str
        """
        self._id = id

    @property
    def zone_name(self):
        """Gets the zone_name of this CreateRetrievalResponse.

        域名名称。

        :return: The zone_name of this CreateRetrievalResponse.
        :rtype: str
        """
        return self._zone_name

    @zone_name.setter
    def zone_name(self, zone_name):
        """Sets the zone_name of this CreateRetrievalResponse.

        域名名称。

        :param zone_name: The zone_name of this CreateRetrievalResponse.
        :type zone_name: str
        """
        self._zone_name = zone_name

    @property
    def record(self):
        """Gets the record of this CreateRetrievalResponse.

        :return: The record of this CreateRetrievalResponse.
        :rtype: :class:`huaweicloudsdkdns.v2.CreatePublicZoneFindRespRecord`
        """
        return self._record

    @record.setter
    def record(self, record):
        """Sets the record of this CreateRetrievalResponse.

        :param record: The record of this CreateRetrievalResponse.
        :type record: :class:`huaweicloudsdkdns.v2.CreatePublicZoneFindRespRecord`
        """
        self._record = record

    @property
    def status(self):
        """Gets the status of this CreateRetrievalResponse.

        状态，(PENDING,VERIFIED,CREATED,EXPIRED)

        :return: The status of this CreateRetrievalResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CreateRetrievalResponse.

        状态，(PENDING,VERIFIED,CREATED,EXPIRED)

        :param status: The status of this CreateRetrievalResponse.
        :type status: str
        """
        self._status = status

    @property
    def created_at(self):
        """Gets the created_at of this CreateRetrievalResponse.

        创建时间。

        :return: The created_at of this CreateRetrievalResponse.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this CreateRetrievalResponse.

        创建时间。

        :param created_at: The created_at of this CreateRetrievalResponse.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this CreateRetrievalResponse.

        更新时间。

        :return: The updated_at of this CreateRetrievalResponse.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this CreateRetrievalResponse.

        更新时间。

        :param updated_at: The updated_at of this CreateRetrievalResponse.
        :type updated_at: str
        """
        self._updated_at = updated_at

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
        if not isinstance(other, CreateRetrievalResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
