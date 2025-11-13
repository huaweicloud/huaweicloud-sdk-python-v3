# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowRetrievalResponse(SdkResponse):

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
        'record': 'RecordInfo',
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
        r"""ShowRetrievalResponse

        The model defined in huaweicloud sdk

        :param id: 找回请求ID。
        :type id: str
        :param zone_name: 域名。
        :type zone_name: str
        :param record: 
        :type record: :class:`huaweicloudsdkdns.v2.RecordInfo`
        :param status: 找回状态。  取值范围：  PENDING：处理中 VERIFIED：已验证 CREATED：已找回 EXPIRED：已失效
        :type status: str
        :param created_at: 创建时间。 格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSS。
        :type created_at: str
        :param updated_at: 更新时间。 格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSS。
        :type updated_at: str
        """
        
        super().__init__()

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
        r"""Gets the id of this ShowRetrievalResponse.

        找回请求ID。

        :return: The id of this ShowRetrievalResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowRetrievalResponse.

        找回请求ID。

        :param id: The id of this ShowRetrievalResponse.
        :type id: str
        """
        self._id = id

    @property
    def zone_name(self):
        r"""Gets the zone_name of this ShowRetrievalResponse.

        域名。

        :return: The zone_name of this ShowRetrievalResponse.
        :rtype: str
        """
        return self._zone_name

    @zone_name.setter
    def zone_name(self, zone_name):
        r"""Sets the zone_name of this ShowRetrievalResponse.

        域名。

        :param zone_name: The zone_name of this ShowRetrievalResponse.
        :type zone_name: str
        """
        self._zone_name = zone_name

    @property
    def record(self):
        r"""Gets the record of this ShowRetrievalResponse.

        :return: The record of this ShowRetrievalResponse.
        :rtype: :class:`huaweicloudsdkdns.v2.RecordInfo`
        """
        return self._record

    @record.setter
    def record(self, record):
        r"""Sets the record of this ShowRetrievalResponse.

        :param record: The record of this ShowRetrievalResponse.
        :type record: :class:`huaweicloudsdkdns.v2.RecordInfo`
        """
        self._record = record

    @property
    def status(self):
        r"""Gets the status of this ShowRetrievalResponse.

        找回状态。  取值范围：  PENDING：处理中 VERIFIED：已验证 CREATED：已找回 EXPIRED：已失效

        :return: The status of this ShowRetrievalResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowRetrievalResponse.

        找回状态。  取值范围：  PENDING：处理中 VERIFIED：已验证 CREATED：已找回 EXPIRED：已失效

        :param status: The status of this ShowRetrievalResponse.
        :type status: str
        """
        self._status = status

    @property
    def created_at(self):
        r"""Gets the created_at of this ShowRetrievalResponse.

        创建时间。 格式：yyyy-MM-dd'T'HH:mm:ss.SSS。

        :return: The created_at of this ShowRetrievalResponse.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this ShowRetrievalResponse.

        创建时间。 格式：yyyy-MM-dd'T'HH:mm:ss.SSS。

        :param created_at: The created_at of this ShowRetrievalResponse.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this ShowRetrievalResponse.

        更新时间。 格式：yyyy-MM-dd'T'HH:mm:ss.SSS。

        :return: The updated_at of this ShowRetrievalResponse.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this ShowRetrievalResponse.

        更新时间。 格式：yyyy-MM-dd'T'HH:mm:ss.SSS。

        :param updated_at: The updated_at of this ShowRetrievalResponse.
        :type updated_at: str
        """
        self._updated_at = updated_at

    def to_dict(self):
        import warnings
        warnings.warn("ShowRetrievalResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShowRetrievalResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
