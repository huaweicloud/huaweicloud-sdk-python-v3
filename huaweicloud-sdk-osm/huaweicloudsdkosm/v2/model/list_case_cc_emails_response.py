# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCaseCcEmailsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cc_email_info': 'IncidentOrderCCEmailInfoV2',
        'mc_email_infos': 'list[str]'
    }

    attribute_map = {
        'cc_email_info': 'cc_email_info',
        'mc_email_infos': 'mc_email_infos'
    }

    def __init__(self, cc_email_info=None, mc_email_infos=None):
        r"""ListCaseCcEmailsResponse

        The model defined in huaweicloud sdk

        :param cc_email_info: 
        :type cc_email_info: :class:`huaweicloudsdkosm.v2.IncidentOrderCCEmailInfoV2`
        :param mc_email_infos: 抄送邮箱信息
        :type mc_email_infos: list[str]
        """
        
        super(ListCaseCcEmailsResponse, self).__init__()

        self._cc_email_info = None
        self._mc_email_infos = None
        self.discriminator = None

        if cc_email_info is not None:
            self.cc_email_info = cc_email_info
        if mc_email_infos is not None:
            self.mc_email_infos = mc_email_infos

    @property
    def cc_email_info(self):
        r"""Gets the cc_email_info of this ListCaseCcEmailsResponse.

        :return: The cc_email_info of this ListCaseCcEmailsResponse.
        :rtype: :class:`huaweicloudsdkosm.v2.IncidentOrderCCEmailInfoV2`
        """
        return self._cc_email_info

    @cc_email_info.setter
    def cc_email_info(self, cc_email_info):
        r"""Sets the cc_email_info of this ListCaseCcEmailsResponse.

        :param cc_email_info: The cc_email_info of this ListCaseCcEmailsResponse.
        :type cc_email_info: :class:`huaweicloudsdkosm.v2.IncidentOrderCCEmailInfoV2`
        """
        self._cc_email_info = cc_email_info

    @property
    def mc_email_infos(self):
        r"""Gets the mc_email_infos of this ListCaseCcEmailsResponse.

        抄送邮箱信息

        :return: The mc_email_infos of this ListCaseCcEmailsResponse.
        :rtype: list[str]
        """
        return self._mc_email_infos

    @mc_email_infos.setter
    def mc_email_infos(self, mc_email_infos):
        r"""Sets the mc_email_infos of this ListCaseCcEmailsResponse.

        抄送邮箱信息

        :param mc_email_infos: The mc_email_infos of this ListCaseCcEmailsResponse.
        :type mc_email_infos: list[str]
        """
        self._mc_email_infos = mc_email_infos

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
        if not isinstance(other, ListCaseCcEmailsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
