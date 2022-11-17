# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSecAppTaskResultResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'basic_info': 'BasicInfo',
        'apk_component_info': 'ApkComponentInfo',
        'hap_component_info': 'HapComponentInfo',
        'vuln_list': 'list[VulnInfo]',
        'privacy_compliance_list': 'list[PrivacyComplianceInfo]'
    }

    attribute_map = {
        'basic_info': 'basic_info',
        'apk_component_info': 'apk_component_info',
        'hap_component_info': 'hap_component_info',
        'vuln_list': 'vuln_list',
        'privacy_compliance_list': 'privacy_compliance_list'
    }

    def __init__(self, basic_info=None, apk_component_info=None, hap_component_info=None, vuln_list=None, privacy_compliance_list=None):
        """ShowSecAppTaskResultResponse

        The model defined in huaweicloud sdk

        :param basic_info: 
        :type basic_info: :class:`huaweicloudsdkdevsecurity.v1.BasicInfo`
        :param apk_component_info: 
        :type apk_component_info: :class:`huaweicloudsdkdevsecurity.v1.ApkComponentInfo`
        :param hap_component_info: 
        :type hap_component_info: :class:`huaweicloudsdkdevsecurity.v1.HapComponentInfo`
        :param vuln_list: 漏洞列表
        :type vuln_list: list[:class:`huaweicloudsdkdevsecurity.v1.VulnInfo`]
        :param privacy_compliance_list: 隐私合规列表
        :type privacy_compliance_list: list[:class:`huaweicloudsdkdevsecurity.v1.PrivacyComplianceInfo`]
        """
        
        super(ShowSecAppTaskResultResponse, self).__init__()

        self._basic_info = None
        self._apk_component_info = None
        self._hap_component_info = None
        self._vuln_list = None
        self._privacy_compliance_list = None
        self.discriminator = None

        if basic_info is not None:
            self.basic_info = basic_info
        if apk_component_info is not None:
            self.apk_component_info = apk_component_info
        if hap_component_info is not None:
            self.hap_component_info = hap_component_info
        if vuln_list is not None:
            self.vuln_list = vuln_list
        if privacy_compliance_list is not None:
            self.privacy_compliance_list = privacy_compliance_list

    @property
    def basic_info(self):
        """Gets the basic_info of this ShowSecAppTaskResultResponse.

        :return: The basic_info of this ShowSecAppTaskResultResponse.
        :rtype: :class:`huaweicloudsdkdevsecurity.v1.BasicInfo`
        """
        return self._basic_info

    @basic_info.setter
    def basic_info(self, basic_info):
        """Sets the basic_info of this ShowSecAppTaskResultResponse.

        :param basic_info: The basic_info of this ShowSecAppTaskResultResponse.
        :type basic_info: :class:`huaweicloudsdkdevsecurity.v1.BasicInfo`
        """
        self._basic_info = basic_info

    @property
    def apk_component_info(self):
        """Gets the apk_component_info of this ShowSecAppTaskResultResponse.

        :return: The apk_component_info of this ShowSecAppTaskResultResponse.
        :rtype: :class:`huaweicloudsdkdevsecurity.v1.ApkComponentInfo`
        """
        return self._apk_component_info

    @apk_component_info.setter
    def apk_component_info(self, apk_component_info):
        """Sets the apk_component_info of this ShowSecAppTaskResultResponse.

        :param apk_component_info: The apk_component_info of this ShowSecAppTaskResultResponse.
        :type apk_component_info: :class:`huaweicloudsdkdevsecurity.v1.ApkComponentInfo`
        """
        self._apk_component_info = apk_component_info

    @property
    def hap_component_info(self):
        """Gets the hap_component_info of this ShowSecAppTaskResultResponse.

        :return: The hap_component_info of this ShowSecAppTaskResultResponse.
        :rtype: :class:`huaweicloudsdkdevsecurity.v1.HapComponentInfo`
        """
        return self._hap_component_info

    @hap_component_info.setter
    def hap_component_info(self, hap_component_info):
        """Sets the hap_component_info of this ShowSecAppTaskResultResponse.

        :param hap_component_info: The hap_component_info of this ShowSecAppTaskResultResponse.
        :type hap_component_info: :class:`huaweicloudsdkdevsecurity.v1.HapComponentInfo`
        """
        self._hap_component_info = hap_component_info

    @property
    def vuln_list(self):
        """Gets the vuln_list of this ShowSecAppTaskResultResponse.

        漏洞列表

        :return: The vuln_list of this ShowSecAppTaskResultResponse.
        :rtype: list[:class:`huaweicloudsdkdevsecurity.v1.VulnInfo`]
        """
        return self._vuln_list

    @vuln_list.setter
    def vuln_list(self, vuln_list):
        """Sets the vuln_list of this ShowSecAppTaskResultResponse.

        漏洞列表

        :param vuln_list: The vuln_list of this ShowSecAppTaskResultResponse.
        :type vuln_list: list[:class:`huaweicloudsdkdevsecurity.v1.VulnInfo`]
        """
        self._vuln_list = vuln_list

    @property
    def privacy_compliance_list(self):
        """Gets the privacy_compliance_list of this ShowSecAppTaskResultResponse.

        隐私合规列表

        :return: The privacy_compliance_list of this ShowSecAppTaskResultResponse.
        :rtype: list[:class:`huaweicloudsdkdevsecurity.v1.PrivacyComplianceInfo`]
        """
        return self._privacy_compliance_list

    @privacy_compliance_list.setter
    def privacy_compliance_list(self, privacy_compliance_list):
        """Sets the privacy_compliance_list of this ShowSecAppTaskResultResponse.

        隐私合规列表

        :param privacy_compliance_list: The privacy_compliance_list of this ShowSecAppTaskResultResponse.
        :type privacy_compliance_list: list[:class:`huaweicloudsdkdevsecurity.v1.PrivacyComplianceInfo`]
        """
        self._privacy_compliance_list = privacy_compliance_list

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
        if not isinstance(other, ShowSecAppTaskResultResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
