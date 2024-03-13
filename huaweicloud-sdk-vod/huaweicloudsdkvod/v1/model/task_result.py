# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskResult:

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
        """TaskResult

        The model defined in huaweicloud sdk

        :param asset_id: 媒资ID 
        :type asset_id: str
        :param status: 修改媒资存储状态任务下发成功与否，SUCCEED成功，FAILED失败 
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
        """Gets the asset_id of this TaskResult.

        媒资ID 

        :return: The asset_id of this TaskResult.
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        """Sets the asset_id of this TaskResult.

        媒资ID 

        :param asset_id: The asset_id of this TaskResult.
        :type asset_id: str
        """
        self._asset_id = asset_id

    @property
    def status(self):
        """Gets the status of this TaskResult.

        修改媒资存储状态任务下发成功与否，SUCCEED成功，FAILED失败 

        :return: The status of this TaskResult.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TaskResult.

        修改媒资存储状态任务下发成功与否，SUCCEED成功，FAILED失败 

        :param status: The status of this TaskResult.
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
        if not isinstance(other, TaskResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
