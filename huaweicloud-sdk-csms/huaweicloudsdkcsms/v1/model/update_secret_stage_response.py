# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateSecretStageResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'stage': 'Stage'
    }

    attribute_map = {
        'stage': 'stage'
    }

    def __init__(self, stage=None):
        """UpdateSecretStageResponse

        The model defined in huaweicloud sdk

        :param stage: 
        :type stage: :class:`huaweicloudsdkcsms.v1.Stage`
        """
        
        super(UpdateSecretStageResponse, self).__init__()

        self._stage = None
        self.discriminator = None

        if stage is not None:
            self.stage = stage

    @property
    def stage(self):
        """Gets the stage of this UpdateSecretStageResponse.


        :return: The stage of this UpdateSecretStageResponse.
        :rtype: :class:`huaweicloudsdkcsms.v1.Stage`
        """
        return self._stage

    @stage.setter
    def stage(self, stage):
        """Sets the stage of this UpdateSecretStageResponse.


        :param stage: The stage of this UpdateSecretStageResponse.
        :type stage: :class:`huaweicloudsdkcsms.v1.Stage`
        """
        self._stage = stage

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
        if not isinstance(other, UpdateSecretStageResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
