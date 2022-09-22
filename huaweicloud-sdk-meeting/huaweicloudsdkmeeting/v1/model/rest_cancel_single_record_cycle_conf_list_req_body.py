# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RestCancelSingleRecordCycleConfListReqBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'cycle_sub_conf_i_ds': 'list[str]'
    }

    attribute_map = {
        'cycle_sub_conf_i_ds': 'cycleSubConfIDs'
    }

    def __init__(self, cycle_sub_conf_i_ds=None):
        """RestCancelSingleRecordCycleConfListReqBody

        The model defined in huaweicloud sdk

        :param cycle_sub_conf_i_ds: 待删除的子会议UUID列表。
        :type cycle_sub_conf_i_ds: list[str]
        """
        
        

        self._cycle_sub_conf_i_ds = None
        self.discriminator = None

        self.cycle_sub_conf_i_ds = cycle_sub_conf_i_ds

    @property
    def cycle_sub_conf_i_ds(self):
        """Gets the cycle_sub_conf_i_ds of this RestCancelSingleRecordCycleConfListReqBody.

        待删除的子会议UUID列表。

        :return: The cycle_sub_conf_i_ds of this RestCancelSingleRecordCycleConfListReqBody.
        :rtype: list[str]
        """
        return self._cycle_sub_conf_i_ds

    @cycle_sub_conf_i_ds.setter
    def cycle_sub_conf_i_ds(self, cycle_sub_conf_i_ds):
        """Sets the cycle_sub_conf_i_ds of this RestCancelSingleRecordCycleConfListReqBody.

        待删除的子会议UUID列表。

        :param cycle_sub_conf_i_ds: The cycle_sub_conf_i_ds of this RestCancelSingleRecordCycleConfListReqBody.
        :type cycle_sub_conf_i_ds: list[str]
        """
        self._cycle_sub_conf_i_ds = cycle_sub_conf_i_ds

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
        if not isinstance(other, RestCancelSingleRecordCycleConfListReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
