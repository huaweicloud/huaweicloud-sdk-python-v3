# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDocWatermarkByAddressRequestBody:

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
        'doc_type': 'str',
        'src_file': 'str',
        'file_password': 'str'
    }

    attribute_map = {
        'region_id': 'region_id',
        'doc_type': 'doc_type',
        'src_file': 'src_file',
        'file_password': 'file_password'
    }

    def __init__(self, region_id=None, doc_type=None, src_file=None, file_password=None):
        """ShowDocWatermarkByAddressRequestBody

        The model defined in huaweicloud sdk

        :param region_id: 项目所在region的id，如：xx-xx-1。
        :type region_id: str
        :param doc_type: 待提取水印的文档类型
        :type doc_type: str
        :param src_file: 待提取文字暗水印的文档的地址，当前只支持华为云OBS对象，格式为 **obs://bucket/object** ，其中bucket为和当前项目处于同一区域的OBS桶名称，object为对象全路径名。例如：**obs://hwbucket/hwinfo/hw.doc**，其中obs://表示OBS存储，hwbucket为桶名，hwinfo/hw.doc为对象全路径名。
        :type src_file: str
        :param file_password: 解密文件的密码， 最大支持长度256。如果Office文档有读密码或域控的权限密码，请输入读密码，或者有读权限的域控密码。
        :type file_password: str
        """
        
        

        self._region_id = None
        self._doc_type = None
        self._src_file = None
        self._file_password = None
        self.discriminator = None

        self.region_id = region_id
        self.doc_type = doc_type
        self.src_file = src_file
        if file_password is not None:
            self.file_password = file_password

    @property
    def region_id(self):
        """Gets the region_id of this ShowDocWatermarkByAddressRequestBody.

        项目所在region的id，如：xx-xx-1。

        :return: The region_id of this ShowDocWatermarkByAddressRequestBody.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this ShowDocWatermarkByAddressRequestBody.

        项目所在region的id，如：xx-xx-1。

        :param region_id: The region_id of this ShowDocWatermarkByAddressRequestBody.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def doc_type(self):
        """Gets the doc_type of this ShowDocWatermarkByAddressRequestBody.

        待提取水印的文档类型

        :return: The doc_type of this ShowDocWatermarkByAddressRequestBody.
        :rtype: str
        """
        return self._doc_type

    @doc_type.setter
    def doc_type(self, doc_type):
        """Sets the doc_type of this ShowDocWatermarkByAddressRequestBody.

        待提取水印的文档类型

        :param doc_type: The doc_type of this ShowDocWatermarkByAddressRequestBody.
        :type doc_type: str
        """
        self._doc_type = doc_type

    @property
    def src_file(self):
        """Gets the src_file of this ShowDocWatermarkByAddressRequestBody.

        待提取文字暗水印的文档的地址，当前只支持华为云OBS对象，格式为 **obs://bucket/object** ，其中bucket为和当前项目处于同一区域的OBS桶名称，object为对象全路径名。例如：**obs://hwbucket/hwinfo/hw.doc**，其中obs://表示OBS存储，hwbucket为桶名，hwinfo/hw.doc为对象全路径名。

        :return: The src_file of this ShowDocWatermarkByAddressRequestBody.
        :rtype: str
        """
        return self._src_file

    @src_file.setter
    def src_file(self, src_file):
        """Sets the src_file of this ShowDocWatermarkByAddressRequestBody.

        待提取文字暗水印的文档的地址，当前只支持华为云OBS对象，格式为 **obs://bucket/object** ，其中bucket为和当前项目处于同一区域的OBS桶名称，object为对象全路径名。例如：**obs://hwbucket/hwinfo/hw.doc**，其中obs://表示OBS存储，hwbucket为桶名，hwinfo/hw.doc为对象全路径名。

        :param src_file: The src_file of this ShowDocWatermarkByAddressRequestBody.
        :type src_file: str
        """
        self._src_file = src_file

    @property
    def file_password(self):
        """Gets the file_password of this ShowDocWatermarkByAddressRequestBody.

        解密文件的密码， 最大支持长度256。如果Office文档有读密码或域控的权限密码，请输入读密码，或者有读权限的域控密码。

        :return: The file_password of this ShowDocWatermarkByAddressRequestBody.
        :rtype: str
        """
        return self._file_password

    @file_password.setter
    def file_password(self, file_password):
        """Sets the file_password of this ShowDocWatermarkByAddressRequestBody.

        解密文件的密码， 最大支持长度256。如果Office文档有读密码或域控的权限密码，请输入读密码，或者有读权限的域控密码。

        :param file_password: The file_password of this ShowDocWatermarkByAddressRequestBody.
        :type file_password: str
        """
        self._file_password = file_password

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
        if not isinstance(other, ShowDocWatermarkByAddressRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
