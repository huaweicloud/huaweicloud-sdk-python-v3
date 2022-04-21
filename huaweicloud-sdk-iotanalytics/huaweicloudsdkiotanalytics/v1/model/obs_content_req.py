# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ObsContentReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'bucket_name': 'str',
        'ak': 'str',
        'sk': 'str'
    }

    attribute_map = {
        'bucket_name': 'bucket_name',
        'ak': 'ak',
        'sk': 'sk'
    }

    def __init__(self, bucket_name=None, ak=None, sk=None):
        """ObsContentReq

        The model defined in huaweicloud sdk

        :param bucket_name: 桶名称
        :type bucket_name: str
        :param ak: 租户的AK
        :type ak: str
        :param sk: 租户的SK
        :type sk: str
        """
        
        

        self._bucket_name = None
        self._ak = None
        self._sk = None
        self.discriminator = None

        self.bucket_name = bucket_name
        self.ak = ak
        self.sk = sk

    @property
    def bucket_name(self):
        """Gets the bucket_name of this ObsContentReq.

        桶名称

        :return: The bucket_name of this ObsContentReq.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        """Sets the bucket_name of this ObsContentReq.

        桶名称

        :param bucket_name: The bucket_name of this ObsContentReq.
        :type bucket_name: str
        """
        self._bucket_name = bucket_name

    @property
    def ak(self):
        """Gets the ak of this ObsContentReq.

        租户的AK

        :return: The ak of this ObsContentReq.
        :rtype: str
        """
        return self._ak

    @ak.setter
    def ak(self, ak):
        """Sets the ak of this ObsContentReq.

        租户的AK

        :param ak: The ak of this ObsContentReq.
        :type ak: str
        """
        self._ak = ak

    @property
    def sk(self):
        """Gets the sk of this ObsContentReq.

        租户的SK

        :return: The sk of this ObsContentReq.
        :rtype: str
        """
        return self._sk

    @sk.setter
    def sk(self, sk):
        """Sets the sk of this ObsContentReq.

        租户的SK

        :param sk: The sk of this ObsContentReq.
        :type sk: str
        """
        self._sk = sk

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
        if not isinstance(other, ObsContentReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
