# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteTableResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'table_id': 'str',
        'process_status': 'IsapTableProcessStatus',
        'delete_time': 'int'
    }

    attribute_map = {
        'table_id': 'table_id',
        'process_status': 'process_status',
        'delete_time': 'delete_time'
    }

    def __init__(self, table_id=None, process_status=None, delete_time=None):
        r"""DeleteTableResponse

        The model defined in huaweicloud sdk

        :param table_id: 表ID
        :type table_id: str
        :param process_status: 
        :type process_status: :class:`huaweicloudsdksecmaster.v2.IsapTableProcessStatus`
        :param delete_time: 毫秒时间戳
        :type delete_time: int
        """
        
        super().__init__()

        self._table_id = None
        self._process_status = None
        self._delete_time = None
        self.discriminator = None

        if table_id is not None:
            self.table_id = table_id
        if process_status is not None:
            self.process_status = process_status
        if delete_time is not None:
            self.delete_time = delete_time

    @property
    def table_id(self):
        r"""Gets the table_id of this DeleteTableResponse.

        表ID

        :return: The table_id of this DeleteTableResponse.
        :rtype: str
        """
        return self._table_id

    @table_id.setter
    def table_id(self, table_id):
        r"""Sets the table_id of this DeleteTableResponse.

        表ID

        :param table_id: The table_id of this DeleteTableResponse.
        :type table_id: str
        """
        self._table_id = table_id

    @property
    def process_status(self):
        r"""Gets the process_status of this DeleteTableResponse.

        :return: The process_status of this DeleteTableResponse.
        :rtype: :class:`huaweicloudsdksecmaster.v2.IsapTableProcessStatus`
        """
        return self._process_status

    @process_status.setter
    def process_status(self, process_status):
        r"""Sets the process_status of this DeleteTableResponse.

        :param process_status: The process_status of this DeleteTableResponse.
        :type process_status: :class:`huaweicloudsdksecmaster.v2.IsapTableProcessStatus`
        """
        self._process_status = process_status

    @property
    def delete_time(self):
        r"""Gets the delete_time of this DeleteTableResponse.

        毫秒时间戳

        :return: The delete_time of this DeleteTableResponse.
        :rtype: int
        """
        return self._delete_time

    @delete_time.setter
    def delete_time(self, delete_time):
        r"""Sets the delete_time of this DeleteTableResponse.

        毫秒时间戳

        :param delete_time: The delete_time of this DeleteTableResponse.
        :type delete_time: int
        """
        self._delete_time = delete_time

    def to_dict(self):
        import warnings
        warnings.warn("DeleteTableResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, DeleteTableResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
