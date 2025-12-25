# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DataObjectBatchUpdateForm:

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
        'trigger_flag': 'bool',
        'data_object': 'object'
    }

    attribute_map = {
        'batch_ids': 'batch_ids',
        'trigger_flag': 'trigger_flag',
        'data_object': 'data_object'
    }

    def __init__(self, batch_ids=None, trigger_flag=None, data_object=None):
        r"""DataObjectBatchUpdateForm

        The model defined in huaweicloud sdk

        :param batch_ids: 批量更新ID列表
        :type batch_ids: list[str]
        :param trigger_flag: 触发标志
        :type trigger_flag: bool
        :param data_object: 数据对象
        :type data_object: object
        """
        
        

        self._batch_ids = None
        self._trigger_flag = None
        self._data_object = None
        self.discriminator = None

        if batch_ids is not None:
            self.batch_ids = batch_ids
        if trigger_flag is not None:
            self.trigger_flag = trigger_flag
        if data_object is not None:
            self.data_object = data_object

    @property
    def batch_ids(self):
        r"""Gets the batch_ids of this DataObjectBatchUpdateForm.

        批量更新ID列表

        :return: The batch_ids of this DataObjectBatchUpdateForm.
        :rtype: list[str]
        """
        return self._batch_ids

    @batch_ids.setter
    def batch_ids(self, batch_ids):
        r"""Sets the batch_ids of this DataObjectBatchUpdateForm.

        批量更新ID列表

        :param batch_ids: The batch_ids of this DataObjectBatchUpdateForm.
        :type batch_ids: list[str]
        """
        self._batch_ids = batch_ids

    @property
    def trigger_flag(self):
        r"""Gets the trigger_flag of this DataObjectBatchUpdateForm.

        触发标志

        :return: The trigger_flag of this DataObjectBatchUpdateForm.
        :rtype: bool
        """
        return self._trigger_flag

    @trigger_flag.setter
    def trigger_flag(self, trigger_flag):
        r"""Sets the trigger_flag of this DataObjectBatchUpdateForm.

        触发标志

        :param trigger_flag: The trigger_flag of this DataObjectBatchUpdateForm.
        :type trigger_flag: bool
        """
        self._trigger_flag = trigger_flag

    @property
    def data_object(self):
        r"""Gets the data_object of this DataObjectBatchUpdateForm.

        数据对象

        :return: The data_object of this DataObjectBatchUpdateForm.
        :rtype: object
        """
        return self._data_object

    @data_object.setter
    def data_object(self, data_object):
        r"""Sets the data_object of this DataObjectBatchUpdateForm.

        数据对象

        :param data_object: The data_object of this DataObjectBatchUpdateForm.
        :type data_object: object
        """
        self._data_object = data_object

    def to_dict(self):
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
        if not isinstance(other, DataObjectBatchUpdateForm):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
