# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CountTasksResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'common_task_details': 'TaskStatisticDetails',
        'cdc_task_details': 'TaskStatisticDetails'
    }

    attribute_map = {
        'common_task_details': 'common_task_details',
        'cdc_task_details': 'cdc_task_details'
    }

    def __init__(self, common_task_details=None, cdc_task_details=None):
        """CountTasksResponse

        The model defined in huaweicloud sdk

        :param common_task_details: 
        :type common_task_details: :class:`huaweicloudsdkroma.v2.TaskStatisticDetails`
        :param cdc_task_details: 
        :type cdc_task_details: :class:`huaweicloudsdkroma.v2.TaskStatisticDetails`
        """
        
        super(CountTasksResponse, self).__init__()

        self._common_task_details = None
        self._cdc_task_details = None
        self.discriminator = None

        if common_task_details is not None:
            self.common_task_details = common_task_details
        if cdc_task_details is not None:
            self.cdc_task_details = cdc_task_details

    @property
    def common_task_details(self):
        """Gets the common_task_details of this CountTasksResponse.


        :return: The common_task_details of this CountTasksResponse.
        :rtype: :class:`huaweicloudsdkroma.v2.TaskStatisticDetails`
        """
        return self._common_task_details

    @common_task_details.setter
    def common_task_details(self, common_task_details):
        """Sets the common_task_details of this CountTasksResponse.


        :param common_task_details: The common_task_details of this CountTasksResponse.
        :type common_task_details: :class:`huaweicloudsdkroma.v2.TaskStatisticDetails`
        """
        self._common_task_details = common_task_details

    @property
    def cdc_task_details(self):
        """Gets the cdc_task_details of this CountTasksResponse.


        :return: The cdc_task_details of this CountTasksResponse.
        :rtype: :class:`huaweicloudsdkroma.v2.TaskStatisticDetails`
        """
        return self._cdc_task_details

    @cdc_task_details.setter
    def cdc_task_details(self, cdc_task_details):
        """Sets the cdc_task_details of this CountTasksResponse.


        :param cdc_task_details: The cdc_task_details of this CountTasksResponse.
        :type cdc_task_details: :class:`huaweicloudsdkroma.v2.TaskStatisticDetails`
        """
        self._cdc_task_details = cdc_task_details

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
        if not isinstance(other, CountTasksResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
