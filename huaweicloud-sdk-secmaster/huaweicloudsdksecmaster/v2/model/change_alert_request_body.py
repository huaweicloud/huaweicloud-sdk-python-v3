# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChangeAlertRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'batch_ids': 'list[str]',
        'data_object': 'Alert'
    }

    attribute_map = {
        'batch_ids': 'batch_ids',
        'data_object': 'data_object'
    }

    def __init__(self, batch_ids=None, data_object=None):
        """ChangeAlertRequestBody

        The model defined in huaweicloud sdk

        :param batch_ids: 更新告警的ID列表
        :type batch_ids: list[str]
        :param data_object: 
        :type data_object: :class:`huaweicloudsdksecmaster.v2.Alert`
        """
        
        

        self._batch_ids = None
        self._data_object = None
        self.discriminator = None

        if batch_ids is not None:
            self.batch_ids = batch_ids
        if data_object is not None:
            self.data_object = data_object

    @property
    def batch_ids(self):
        """Gets the batch_ids of this ChangeAlertRequestBody.

        更新告警的ID列表

        :return: The batch_ids of this ChangeAlertRequestBody.
        :rtype: list[str]
        """
        return self._batch_ids

    @batch_ids.setter
    def batch_ids(self, batch_ids):
        """Sets the batch_ids of this ChangeAlertRequestBody.

        更新告警的ID列表

        :param batch_ids: The batch_ids of this ChangeAlertRequestBody.
        :type batch_ids: list[str]
        """
        self._batch_ids = batch_ids

    @property
    def data_object(self):
        """Gets the data_object of this ChangeAlertRequestBody.

        :return: The data_object of this ChangeAlertRequestBody.
        :rtype: :class:`huaweicloudsdksecmaster.v2.Alert`
        """
        return self._data_object

    @data_object.setter
    def data_object(self, data_object):
        """Sets the data_object of this ChangeAlertRequestBody.

        :param data_object: The data_object of this ChangeAlertRequestBody.
        :type data_object: :class:`huaweicloudsdksecmaster.v2.Alert`
        """
        self._data_object = data_object

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
        if not isinstance(other, ChangeAlertRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
