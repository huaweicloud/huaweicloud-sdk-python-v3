# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteTrackerRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'tracker_name': 'str',
        'tracker_type': 'str'
    }

    attribute_map = {
        'tracker_name': 'tracker_name',
        'tracker_type': 'tracker_type'
    }

    def __init__(self, tracker_name=None, tracker_type=None):
        """DeleteTrackerRequest

        The model defined in huaweicloud sdk

        :param tracker_name: 标识追踪器名称。 在不传入该字段的情况下，将删除当前租户所有的数据类追踪器。
        :type tracker_name: str
        :param tracker_type: 标识追踪器类型。 目前仅支持数据类追踪器（data）的删除，默认值为\&quot;data\&quot;。
        :type tracker_type: str
        """
        
        

        self._tracker_name = None
        self._tracker_type = None
        self.discriminator = None

        if tracker_name is not None:
            self.tracker_name = tracker_name
        if tracker_type is not None:
            self.tracker_type = tracker_type

    @property
    def tracker_name(self):
        """Gets the tracker_name of this DeleteTrackerRequest.

        标识追踪器名称。 在不传入该字段的情况下，将删除当前租户所有的数据类追踪器。

        :return: The tracker_name of this DeleteTrackerRequest.
        :rtype: str
        """
        return self._tracker_name

    @tracker_name.setter
    def tracker_name(self, tracker_name):
        """Sets the tracker_name of this DeleteTrackerRequest.

        标识追踪器名称。 在不传入该字段的情况下，将删除当前租户所有的数据类追踪器。

        :param tracker_name: The tracker_name of this DeleteTrackerRequest.
        :type tracker_name: str
        """
        self._tracker_name = tracker_name

    @property
    def tracker_type(self):
        """Gets the tracker_type of this DeleteTrackerRequest.

        标识追踪器类型。 目前仅支持数据类追踪器（data）的删除，默认值为\"data\"。

        :return: The tracker_type of this DeleteTrackerRequest.
        :rtype: str
        """
        return self._tracker_type

    @tracker_type.setter
    def tracker_type(self, tracker_type):
        """Sets the tracker_type of this DeleteTrackerRequest.

        标识追踪器类型。 目前仅支持数据类追踪器（data）的删除，默认值为\"data\"。

        :param tracker_type: The tracker_type of this DeleteTrackerRequest.
        :type tracker_type: str
        """
        self._tracker_type = tracker_type

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
        if not isinstance(other, DeleteTrackerRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
