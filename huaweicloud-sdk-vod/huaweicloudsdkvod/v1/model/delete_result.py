# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'asset_id': 'str',
        'status': 'str'
    }

    attribute_map = {
        'asset_id': 'asset_id',
        'status': 'status'
    }

    def __init__(self, asset_id=None, status=None):
        r"""DeleteResult

        The model defined in huaweicloud sdk

        :param asset_id: 媒资ID。
        :type asset_id: str
        :param status: 删除状态。  取值如下： - DELETED：已删除。 - FAILED：删除失败。
        :type status: str
        """
        
        

        self._asset_id = None
        self._status = None
        self.discriminator = None

        if asset_id is not None:
            self.asset_id = asset_id
        if status is not None:
            self.status = status

    @property
    def asset_id(self):
        r"""Gets the asset_id of this DeleteResult.

        媒资ID。

        :return: The asset_id of this DeleteResult.
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        r"""Sets the asset_id of this DeleteResult.

        媒资ID。

        :param asset_id: The asset_id of this DeleteResult.
        :type asset_id: str
        """
        self._asset_id = asset_id

    @property
    def status(self):
        r"""Gets the status of this DeleteResult.

        删除状态。  取值如下： - DELETED：已删除。 - FAILED：删除失败。

        :return: The status of this DeleteResult.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this DeleteResult.

        删除状态。  取值如下： - DELETED：已删除。 - FAILED：删除失败。

        :param status: The status of this DeleteResult.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, DeleteResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
