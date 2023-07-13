# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListLabelsAomPromGetResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'data': 'list[str]'
    }

    attribute_map = {
        'status': 'status',
        'data': 'data'
    }

    def __init__(self, status=None, data=None):
        """ListLabelsAomPromGetResponse

        The model defined in huaweicloud sdk

        :param status: 响应状态。
        :type status: str
        :param data: 标签值信息。
        :type data: list[str]
        """
        
        super(ListLabelsAomPromGetResponse, self).__init__()

        self._status = None
        self._data = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if data is not None:
            self.data = data

    @property
    def status(self):
        """Gets the status of this ListLabelsAomPromGetResponse.

        响应状态。

        :return: The status of this ListLabelsAomPromGetResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListLabelsAomPromGetResponse.

        响应状态。

        :param status: The status of this ListLabelsAomPromGetResponse.
        :type status: str
        """
        self._status = status

    @property
    def data(self):
        """Gets the data of this ListLabelsAomPromGetResponse.

        标签值信息。

        :return: The data of this ListLabelsAomPromGetResponse.
        :rtype: list[str]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this ListLabelsAomPromGetResponse.

        标签值信息。

        :param data: The data of this ListLabelsAomPromGetResponse.
        :type data: list[str]
        """
        self._data = data

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
        if not isinstance(other, ListLabelsAomPromGetResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
