# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateDocWatermarkByAddressResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'region_id': 'str',
        'watermarked_file': 'str'
    }

    attribute_map = {
        'region_id': 'region_id',
        'watermarked_file': 'watermarked_file'
    }

    def __init__(self, region_id=None, watermarked_file=None):
        """CreateDocWatermarkByAddressResponse

        The model defined in huaweicloud sdk

        :param region_id: 当前项目所在region的id，如：xx-xx-1。
        :type region_id: str
        :param watermarked_file: 添加水印后的文档地址，当前只支持华为云OBS对象，格式为 **obs://bucket/object** ，其中bucket为和当前项目处于同一区域的OBS桶名称，object为对象全路径名。例如：**obs://hwbucket/hwinfo/hw.doc**，其中obs://表示OBS存储，hwbucket为桶名，hwinfo/hw.doc为对象全路径名。
        :type watermarked_file: str
        """
        
        super(CreateDocWatermarkByAddressResponse, self).__init__()

        self._region_id = None
        self._watermarked_file = None
        self.discriminator = None

        if region_id is not None:
            self.region_id = region_id
        if watermarked_file is not None:
            self.watermarked_file = watermarked_file

    @property
    def region_id(self):
        """Gets the region_id of this CreateDocWatermarkByAddressResponse.

        当前项目所在region的id，如：xx-xx-1。

        :return: The region_id of this CreateDocWatermarkByAddressResponse.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this CreateDocWatermarkByAddressResponse.

        当前项目所在region的id，如：xx-xx-1。

        :param region_id: The region_id of this CreateDocWatermarkByAddressResponse.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def watermarked_file(self):
        """Gets the watermarked_file of this CreateDocWatermarkByAddressResponse.

        添加水印后的文档地址，当前只支持华为云OBS对象，格式为 **obs://bucket/object** ，其中bucket为和当前项目处于同一区域的OBS桶名称，object为对象全路径名。例如：**obs://hwbucket/hwinfo/hw.doc**，其中obs://表示OBS存储，hwbucket为桶名，hwinfo/hw.doc为对象全路径名。

        :return: The watermarked_file of this CreateDocWatermarkByAddressResponse.
        :rtype: str
        """
        return self._watermarked_file

    @watermarked_file.setter
    def watermarked_file(self, watermarked_file):
        """Sets the watermarked_file of this CreateDocWatermarkByAddressResponse.

        添加水印后的文档地址，当前只支持华为云OBS对象，格式为 **obs://bucket/object** ，其中bucket为和当前项目处于同一区域的OBS桶名称，object为对象全路径名。例如：**obs://hwbucket/hwinfo/hw.doc**，其中obs://表示OBS存储，hwbucket为桶名，hwinfo/hw.doc为对象全路径名。

        :param watermarked_file: The watermarked_file of this CreateDocWatermarkByAddressResponse.
        :type watermarked_file: str
        """
        self._watermarked_file = watermarked_file

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
        if not isinstance(other, CreateDocWatermarkByAddressResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
