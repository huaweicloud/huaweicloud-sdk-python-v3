# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateLtsInfoConfigRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'enabale': 'bool',
        'lts_id_info': 'LtsIdInfo'
    }

    attribute_map = {
        'enabale': 'enabale',
        'lts_id_info': 'ltsIdInfo'
    }

    def __init__(self, enabale=None, lts_id_info=None):
        """UpdateLtsInfoConfigRequestBody

        The model defined in huaweicloud sdk

        :param enabale: 是否开启全量日志   - false: 不开启   - true: 开启
        :type enabale: bool
        :param lts_id_info: 
        :type lts_id_info: :class:`huaweicloudsdkwaf.v1.LtsIdInfo`
        """
        
        

        self._enabale = None
        self._lts_id_info = None
        self.discriminator = None

        self.enabale = enabale
        if lts_id_info is not None:
            self.lts_id_info = lts_id_info

    @property
    def enabale(self):
        """Gets the enabale of this UpdateLtsInfoConfigRequestBody.

        是否开启全量日志   - false: 不开启   - true: 开启

        :return: The enabale of this UpdateLtsInfoConfigRequestBody.
        :rtype: bool
        """
        return self._enabale

    @enabale.setter
    def enabale(self, enabale):
        """Sets the enabale of this UpdateLtsInfoConfigRequestBody.

        是否开启全量日志   - false: 不开启   - true: 开启

        :param enabale: The enabale of this UpdateLtsInfoConfigRequestBody.
        :type enabale: bool
        """
        self._enabale = enabale

    @property
    def lts_id_info(self):
        """Gets the lts_id_info of this UpdateLtsInfoConfigRequestBody.


        :return: The lts_id_info of this UpdateLtsInfoConfigRequestBody.
        :rtype: :class:`huaweicloudsdkwaf.v1.LtsIdInfo`
        """
        return self._lts_id_info

    @lts_id_info.setter
    def lts_id_info(self, lts_id_info):
        """Sets the lts_id_info of this UpdateLtsInfoConfigRequestBody.


        :param lts_id_info: The lts_id_info of this UpdateLtsInfoConfigRequestBody.
        :type lts_id_info: :class:`huaweicloudsdkwaf.v1.LtsIdInfo`
        """
        self._lts_id_info = lts_id_info

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
        if not isinstance(other, UpdateLtsInfoConfigRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
