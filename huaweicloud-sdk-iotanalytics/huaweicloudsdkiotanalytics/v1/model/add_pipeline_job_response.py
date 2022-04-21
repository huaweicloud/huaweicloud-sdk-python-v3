# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddPipelineJobResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'pipeline_id': 'str',
        'check_info': 'dict(str, object)'
    }

    attribute_map = {
        'pipeline_id': 'pipeline_id',
        'check_info': 'check_info'
    }

    def __init__(self, pipeline_id=None, check_info=None):
        """AddPipelineJobResponse

        The model defined in huaweicloud sdk

        :param pipeline_id: 管道ID
        :type pipeline_id: str
        :param check_info: 管道错误详情
        :type check_info: dict(str, object)
        """
        
        super(AddPipelineJobResponse, self).__init__()

        self._pipeline_id = None
        self._check_info = None
        self.discriminator = None

        if pipeline_id is not None:
            self.pipeline_id = pipeline_id
        if check_info is not None:
            self.check_info = check_info

    @property
    def pipeline_id(self):
        """Gets the pipeline_id of this AddPipelineJobResponse.

        管道ID

        :return: The pipeline_id of this AddPipelineJobResponse.
        :rtype: str
        """
        return self._pipeline_id

    @pipeline_id.setter
    def pipeline_id(self, pipeline_id):
        """Sets the pipeline_id of this AddPipelineJobResponse.

        管道ID

        :param pipeline_id: The pipeline_id of this AddPipelineJobResponse.
        :type pipeline_id: str
        """
        self._pipeline_id = pipeline_id

    @property
    def check_info(self):
        """Gets the check_info of this AddPipelineJobResponse.

        管道错误详情

        :return: The check_info of this AddPipelineJobResponse.
        :rtype: dict(str, object)
        """
        return self._check_info

    @check_info.setter
    def check_info(self, check_info):
        """Sets the check_info of this AddPipelineJobResponse.

        管道错误详情

        :param check_info: The check_info of this AddPipelineJobResponse.
        :type check_info: dict(str, object)
        """
        self._check_info = check_info

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
        if not isinstance(other, AddPipelineJobResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
