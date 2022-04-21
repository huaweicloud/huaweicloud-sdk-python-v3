# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UploadMetaDataByUrlReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'upload_metadatas': 'list[UploadMetaDataByUrl]'
    }

    attribute_map = {
        'upload_metadatas': 'upload_metadatas'
    }

    def __init__(self, upload_metadatas=None):
        """UploadMetaDataByUrlReq

        The model defined in huaweicloud sdk

        :param upload_metadatas: 待拉取创建的媒资元数据
        :type upload_metadatas: list[:class:`huaweicloudsdkvod.v1.UploadMetaDataByUrl`]
        """
        
        

        self._upload_metadatas = None
        self.discriminator = None

        self.upload_metadatas = upload_metadatas

    @property
    def upload_metadatas(self):
        """Gets the upload_metadatas of this UploadMetaDataByUrlReq.

        待拉取创建的媒资元数据

        :return: The upload_metadatas of this UploadMetaDataByUrlReq.
        :rtype: list[:class:`huaweicloudsdkvod.v1.UploadMetaDataByUrl`]
        """
        return self._upload_metadatas

    @upload_metadatas.setter
    def upload_metadatas(self, upload_metadatas):
        """Sets the upload_metadatas of this UploadMetaDataByUrlReq.

        待拉取创建的媒资元数据

        :param upload_metadatas: The upload_metadatas of this UploadMetaDataByUrlReq.
        :type upload_metadatas: list[:class:`huaweicloudsdkvod.v1.UploadMetaDataByUrl`]
        """
        self._upload_metadatas = upload_metadatas

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
        if not isinstance(other, UploadMetaDataByUrlReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
