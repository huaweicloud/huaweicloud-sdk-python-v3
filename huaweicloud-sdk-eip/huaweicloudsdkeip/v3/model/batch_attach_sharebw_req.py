# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchAttachSharebwReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'publicips': 'list[BatchAttachSharebwDict]'
    }

    attribute_map = {
        'publicips': 'publicips'
    }

    def __init__(self, publicips=None):
        r"""BatchAttachSharebwReq

        The model defined in huaweicloud sdk

        :param publicips: - 功能说明：共享带宽数据 - 约束：共享带宽批量加入多个弹性公网IP时，请求参数publicips中的bandwidth_id必须为同一个共享带宽的id
        :type publicips: list[:class:`huaweicloudsdkeip.v3.BatchAttachSharebwDict`]
        """
        
        

        self._publicips = None
        self.discriminator = None

        if publicips is not None:
            self.publicips = publicips

    @property
    def publicips(self):
        r"""Gets the publicips of this BatchAttachSharebwReq.

        - 功能说明：共享带宽数据 - 约束：共享带宽批量加入多个弹性公网IP时，请求参数publicips中的bandwidth_id必须为同一个共享带宽的id

        :return: The publicips of this BatchAttachSharebwReq.
        :rtype: list[:class:`huaweicloudsdkeip.v3.BatchAttachSharebwDict`]
        """
        return self._publicips

    @publicips.setter
    def publicips(self, publicips):
        r"""Sets the publicips of this BatchAttachSharebwReq.

        - 功能说明：共享带宽数据 - 约束：共享带宽批量加入多个弹性公网IP时，请求参数publicips中的bandwidth_id必须为同一个共享带宽的id

        :param publicips: The publicips of this BatchAttachSharebwReq.
        :type publicips: list[:class:`huaweicloudsdkeip.v3.BatchAttachSharebwDict`]
        """
        self._publicips = publicips

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
        if not isinstance(other, BatchAttachSharebwReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
