# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetServiceLinkedAgencyDeletionStatusV5Request:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'deletion_task_id': 'str'
    }

    attribute_map = {
        'deletion_task_id': 'deletion_task_id'
    }

    def __init__(self, deletion_task_id=None):
        r"""GetServiceLinkedAgencyDeletionStatusV5Request

        The model defined in huaweicloud sdk

        :param deletion_task_id: 删除任务ID。
        :type deletion_task_id: str
        """
        
        

        self._deletion_task_id = None
        self.discriminator = None

        self.deletion_task_id = deletion_task_id

    @property
    def deletion_task_id(self):
        r"""Gets the deletion_task_id of this GetServiceLinkedAgencyDeletionStatusV5Request.

        删除任务ID。

        :return: The deletion_task_id of this GetServiceLinkedAgencyDeletionStatusV5Request.
        :rtype: str
        """
        return self._deletion_task_id

    @deletion_task_id.setter
    def deletion_task_id(self, deletion_task_id):
        r"""Sets the deletion_task_id of this GetServiceLinkedAgencyDeletionStatusV5Request.

        删除任务ID。

        :param deletion_task_id: The deletion_task_id of this GetServiceLinkedAgencyDeletionStatusV5Request.
        :type deletion_task_id: str
        """
        self._deletion_task_id = deletion_task_id

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
        if not isinstance(other, GetServiceLinkedAgencyDeletionStatusV5Request):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
