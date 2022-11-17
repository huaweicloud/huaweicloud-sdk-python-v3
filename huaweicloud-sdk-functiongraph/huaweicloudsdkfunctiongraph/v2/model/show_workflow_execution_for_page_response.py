# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowWorkflowExecutionForPageResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'pager': 'Pager',
        'his_records': 'FlowExecutionBriefV2'
    }

    attribute_map = {
        'pager': 'pager',
        'his_records': 'hisRecords'
    }

    def __init__(self, pager=None, his_records=None):
        """ShowWorkflowExecutionForPageResponse

        The model defined in huaweicloud sdk

        :param pager: 
        :type pager: :class:`huaweicloudsdkfunctiongraph.v2.Pager`
        :param his_records: 
        :type his_records: :class:`huaweicloudsdkfunctiongraph.v2.FlowExecutionBriefV2`
        """
        
        super(ShowWorkflowExecutionForPageResponse, self).__init__()

        self._pager = None
        self._his_records = None
        self.discriminator = None

        if pager is not None:
            self.pager = pager
        if his_records is not None:
            self.his_records = his_records

    @property
    def pager(self):
        """Gets the pager of this ShowWorkflowExecutionForPageResponse.

        :return: The pager of this ShowWorkflowExecutionForPageResponse.
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.Pager`
        """
        return self._pager

    @pager.setter
    def pager(self, pager):
        """Sets the pager of this ShowWorkflowExecutionForPageResponse.

        :param pager: The pager of this ShowWorkflowExecutionForPageResponse.
        :type pager: :class:`huaweicloudsdkfunctiongraph.v2.Pager`
        """
        self._pager = pager

    @property
    def his_records(self):
        """Gets the his_records of this ShowWorkflowExecutionForPageResponse.

        :return: The his_records of this ShowWorkflowExecutionForPageResponse.
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.FlowExecutionBriefV2`
        """
        return self._his_records

    @his_records.setter
    def his_records(self, his_records):
        """Sets the his_records of this ShowWorkflowExecutionForPageResponse.

        :param his_records: The his_records of this ShowWorkflowExecutionForPageResponse.
        :type his_records: :class:`huaweicloudsdkfunctiongraph.v2.FlowExecutionBriefV2`
        """
        self._his_records = his_records

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
        if not isinstance(other, ShowWorkflowExecutionForPageResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
