# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TuningParamInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'full_sync': 'list[TuningParameter]',
        'incre_capture': 'list[TuningParameter]',
        'incre_apply': 'list[TuningParameter]',
        'incre_relay': 'list[TuningParameter]'
    }

    attribute_map = {
        'full_sync': 'full_sync',
        'incre_capture': 'incre_capture',
        'incre_apply': 'incre_apply',
        'incre_relay': 'incre_relay'
    }

    def __init__(self, full_sync=None, incre_capture=None, incre_apply=None, incre_relay=None):
        """TuningParamInfo

        The model defined in huaweicloud sdk

        :param full_sync: 全量调优参数。
        :type full_sync: list[:class:`huaweicloudsdkdrs.v5.TuningParameter`]
        :param incre_capture: 增量抓取调优参数。
        :type incre_capture: list[:class:`huaweicloudsdkdrs.v5.TuningParameter`]
        :param incre_apply: 增量回放调优参数。
        :type incre_apply: list[:class:`huaweicloudsdkdrs.v5.TuningParameter`]
        :param incre_relay: 增量日志拉取调优参数。
        :type incre_relay: list[:class:`huaweicloudsdkdrs.v5.TuningParameter`]
        """
        
        

        self._full_sync = None
        self._incre_capture = None
        self._incre_apply = None
        self._incre_relay = None
        self.discriminator = None

        self.full_sync = full_sync
        self.incre_capture = incre_capture
        self.incre_apply = incre_apply
        self.incre_relay = incre_relay

    @property
    def full_sync(self):
        """Gets the full_sync of this TuningParamInfo.

        全量调优参数。

        :return: The full_sync of this TuningParamInfo.
        :rtype: list[:class:`huaweicloudsdkdrs.v5.TuningParameter`]
        """
        return self._full_sync

    @full_sync.setter
    def full_sync(self, full_sync):
        """Sets the full_sync of this TuningParamInfo.

        全量调优参数。

        :param full_sync: The full_sync of this TuningParamInfo.
        :type full_sync: list[:class:`huaweicloudsdkdrs.v5.TuningParameter`]
        """
        self._full_sync = full_sync

    @property
    def incre_capture(self):
        """Gets the incre_capture of this TuningParamInfo.

        增量抓取调优参数。

        :return: The incre_capture of this TuningParamInfo.
        :rtype: list[:class:`huaweicloudsdkdrs.v5.TuningParameter`]
        """
        return self._incre_capture

    @incre_capture.setter
    def incre_capture(self, incre_capture):
        """Sets the incre_capture of this TuningParamInfo.

        增量抓取调优参数。

        :param incre_capture: The incre_capture of this TuningParamInfo.
        :type incre_capture: list[:class:`huaweicloudsdkdrs.v5.TuningParameter`]
        """
        self._incre_capture = incre_capture

    @property
    def incre_apply(self):
        """Gets the incre_apply of this TuningParamInfo.

        增量回放调优参数。

        :return: The incre_apply of this TuningParamInfo.
        :rtype: list[:class:`huaweicloudsdkdrs.v5.TuningParameter`]
        """
        return self._incre_apply

    @incre_apply.setter
    def incre_apply(self, incre_apply):
        """Sets the incre_apply of this TuningParamInfo.

        增量回放调优参数。

        :param incre_apply: The incre_apply of this TuningParamInfo.
        :type incre_apply: list[:class:`huaweicloudsdkdrs.v5.TuningParameter`]
        """
        self._incre_apply = incre_apply

    @property
    def incre_relay(self):
        """Gets the incre_relay of this TuningParamInfo.

        增量日志拉取调优参数。

        :return: The incre_relay of this TuningParamInfo.
        :rtype: list[:class:`huaweicloudsdkdrs.v5.TuningParameter`]
        """
        return self._incre_relay

    @incre_relay.setter
    def incre_relay(self, incre_relay):
        """Sets the incre_relay of this TuningParamInfo.

        增量日志拉取调优参数。

        :param incre_relay: The incre_relay of this TuningParamInfo.
        :type incre_relay: list[:class:`huaweicloudsdkdrs.v5.TuningParameter`]
        """
        self._incre_relay = incre_relay

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
        if not isinstance(other, TuningParamInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
