# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UploadKieRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'upload_file': 'file'
    }

    attribute_map = {
        'upload_file': 'upload_file'
    }

    def __init__(self, upload_file=None):
        """UploadKieRequestBody

        The model defined in huaweicloud sdk

        :param upload_file: 导入文件内容的格式必须为键值对映射，例如:{\&quot;data\&quot;:[{\&quot;key1\&quot;:\&quot;value1\&quot;,\&quot;key2\&quot;:\&quot;value2\&quot;}]}}
        :type upload_file: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        """
        
        

        self._upload_file = None
        self.discriminator = None

        self.upload_file = upload_file

    @property
    def upload_file(self):
        """Gets the upload_file of this UploadKieRequestBody.

        导入文件内容的格式必须为键值对映射，例如:{\"data\":[{\"key1\":\"value1\",\"key2\":\"value2\"}]}}

        :return: The upload_file of this UploadKieRequestBody.
        :rtype: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        """
        return self._upload_file

    @upload_file.setter
    def upload_file(self, upload_file):
        """Sets the upload_file of this UploadKieRequestBody.

        导入文件内容的格式必须为键值对映射，例如:{\"data\":[{\"key1\":\"value1\",\"key2\":\"value2\"}]}}

        :param upload_file: The upload_file of this UploadKieRequestBody.
        :type upload_file: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        """
        self._upload_file = upload_file

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
        if not isinstance(other, UploadKieRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
