# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CdmStopClusterReqStop:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'stop_mode': 'str',
        'delay_time': 'int'
    }

    attribute_map = {
        'stop_mode': 'stopMode',
        'delay_time': 'delayTime'
    }

    def __init__(self, stop_mode=None, delay_time=None):
        r"""CdmStopClusterReqStop

        The model defined in huaweicloud sdk

        :param stop_mode: 关机类型： - IMMEDIATELY：立即关机。 - GRACEFULLY：优雅关机。
        :type stop_mode: str
        :param delay_time: 关机时延，仅在stopMode为“GRACEFULLY”生效，单位：秒。该值为-1时，表示等待所有作业完成，并停止接受新作业。该值为大于0的任意值表示等待该时长后关机，并停止接受新作业。
        :type delay_time: int
        """
        
        

        self._stop_mode = None
        self._delay_time = None
        self.discriminator = None

        self.stop_mode = stop_mode
        if delay_time is not None:
            self.delay_time = delay_time

    @property
    def stop_mode(self):
        r"""Gets the stop_mode of this CdmStopClusterReqStop.

        关机类型： - IMMEDIATELY：立即关机。 - GRACEFULLY：优雅关机。

        :return: The stop_mode of this CdmStopClusterReqStop.
        :rtype: str
        """
        return self._stop_mode

    @stop_mode.setter
    def stop_mode(self, stop_mode):
        r"""Sets the stop_mode of this CdmStopClusterReqStop.

        关机类型： - IMMEDIATELY：立即关机。 - GRACEFULLY：优雅关机。

        :param stop_mode: The stop_mode of this CdmStopClusterReqStop.
        :type stop_mode: str
        """
        self._stop_mode = stop_mode

    @property
    def delay_time(self):
        r"""Gets the delay_time of this CdmStopClusterReqStop.

        关机时延，仅在stopMode为“GRACEFULLY”生效，单位：秒。该值为-1时，表示等待所有作业完成，并停止接受新作业。该值为大于0的任意值表示等待该时长后关机，并停止接受新作业。

        :return: The delay_time of this CdmStopClusterReqStop.
        :rtype: int
        """
        return self._delay_time

    @delay_time.setter
    def delay_time(self, delay_time):
        r"""Sets the delay_time of this CdmStopClusterReqStop.

        关机时延，仅在stopMode为“GRACEFULLY”生效，单位：秒。该值为-1时，表示等待所有作业完成，并停止接受新作业。该值为大于0的任意值表示等待该时长后关机，并停止接受新作业。

        :param delay_time: The delay_time of this CdmStopClusterReqStop.
        :type delay_time: int
        """
        self._delay_time = delay_time

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
        if not isinstance(other, CdmStopClusterReqStop):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
