# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EstimateDesktopPoolResizeResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_upgrade': 'bool',
        'batch_inquiry_rsp_when_upgrade': 'PeriodBatchUpChangeResourceRsp',
        'batch_inquiry_rsp_when_downgrade': 'BatchInquiryChangeRsp'
    }

    attribute_map = {
        'is_upgrade': 'is_upgrade',
        'batch_inquiry_rsp_when_upgrade': 'batch_inquiry_rsp_when_upgrade',
        'batch_inquiry_rsp_when_downgrade': 'batch_inquiry_rsp_when_downgrade'
    }

    def __init__(self, is_upgrade=None, batch_inquiry_rsp_when_upgrade=None, batch_inquiry_rsp_when_downgrade=None):
        r"""EstimateDesktopPoolResizeResponse

        The model defined in huaweicloud sdk

        :param is_upgrade: 是否为升配。
        :type is_upgrade: bool
        :param batch_inquiry_rsp_when_upgrade: 
        :type batch_inquiry_rsp_when_upgrade: :class:`huaweicloudsdkworkspace.v2.PeriodBatchUpChangeResourceRsp`
        :param batch_inquiry_rsp_when_downgrade: 
        :type batch_inquiry_rsp_when_downgrade: :class:`huaweicloudsdkworkspace.v2.BatchInquiryChangeRsp`
        """
        
        super(EstimateDesktopPoolResizeResponse, self).__init__()

        self._is_upgrade = None
        self._batch_inquiry_rsp_when_upgrade = None
        self._batch_inquiry_rsp_when_downgrade = None
        self.discriminator = None

        if is_upgrade is not None:
            self.is_upgrade = is_upgrade
        if batch_inquiry_rsp_when_upgrade is not None:
            self.batch_inquiry_rsp_when_upgrade = batch_inquiry_rsp_when_upgrade
        if batch_inquiry_rsp_when_downgrade is not None:
            self.batch_inquiry_rsp_when_downgrade = batch_inquiry_rsp_when_downgrade

    @property
    def is_upgrade(self):
        r"""Gets the is_upgrade of this EstimateDesktopPoolResizeResponse.

        是否为升配。

        :return: The is_upgrade of this EstimateDesktopPoolResizeResponse.
        :rtype: bool
        """
        return self._is_upgrade

    @is_upgrade.setter
    def is_upgrade(self, is_upgrade):
        r"""Sets the is_upgrade of this EstimateDesktopPoolResizeResponse.

        是否为升配。

        :param is_upgrade: The is_upgrade of this EstimateDesktopPoolResizeResponse.
        :type is_upgrade: bool
        """
        self._is_upgrade = is_upgrade

    @property
    def batch_inquiry_rsp_when_upgrade(self):
        r"""Gets the batch_inquiry_rsp_when_upgrade of this EstimateDesktopPoolResizeResponse.

        :return: The batch_inquiry_rsp_when_upgrade of this EstimateDesktopPoolResizeResponse.
        :rtype: :class:`huaweicloudsdkworkspace.v2.PeriodBatchUpChangeResourceRsp`
        """
        return self._batch_inquiry_rsp_when_upgrade

    @batch_inquiry_rsp_when_upgrade.setter
    def batch_inquiry_rsp_when_upgrade(self, batch_inquiry_rsp_when_upgrade):
        r"""Sets the batch_inquiry_rsp_when_upgrade of this EstimateDesktopPoolResizeResponse.

        :param batch_inquiry_rsp_when_upgrade: The batch_inquiry_rsp_when_upgrade of this EstimateDesktopPoolResizeResponse.
        :type batch_inquiry_rsp_when_upgrade: :class:`huaweicloudsdkworkspace.v2.PeriodBatchUpChangeResourceRsp`
        """
        self._batch_inquiry_rsp_when_upgrade = batch_inquiry_rsp_when_upgrade

    @property
    def batch_inquiry_rsp_when_downgrade(self):
        r"""Gets the batch_inquiry_rsp_when_downgrade of this EstimateDesktopPoolResizeResponse.

        :return: The batch_inquiry_rsp_when_downgrade of this EstimateDesktopPoolResizeResponse.
        :rtype: :class:`huaweicloudsdkworkspace.v2.BatchInquiryChangeRsp`
        """
        return self._batch_inquiry_rsp_when_downgrade

    @batch_inquiry_rsp_when_downgrade.setter
    def batch_inquiry_rsp_when_downgrade(self, batch_inquiry_rsp_when_downgrade):
        r"""Sets the batch_inquiry_rsp_when_downgrade of this EstimateDesktopPoolResizeResponse.

        :param batch_inquiry_rsp_when_downgrade: The batch_inquiry_rsp_when_downgrade of this EstimateDesktopPoolResizeResponse.
        :type batch_inquiry_rsp_when_downgrade: :class:`huaweicloudsdkworkspace.v2.BatchInquiryChangeRsp`
        """
        self._batch_inquiry_rsp_when_downgrade = batch_inquiry_rsp_when_downgrade

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
        if not isinstance(other, EstimateDesktopPoolResizeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
