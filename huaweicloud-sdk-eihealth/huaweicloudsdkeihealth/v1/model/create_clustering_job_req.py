# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateClusteringJobReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'basic_info': 'CreateDrugJobBasicInfo',
        'file': 'ClusteringDrugFile'
    }

    attribute_map = {
        'basic_info': 'basic_info',
        'file': 'file'
    }

    def __init__(self, basic_info=None, file=None):
        r"""CreateClusteringJobReq

        The model defined in huaweicloud sdk

        :param basic_info: 
        :type basic_info: :class:`huaweicloudsdkeihealth.v1.CreateDrugJobBasicInfo`
        :param file: 
        :type file: :class:`huaweicloudsdkeihealth.v1.ClusteringDrugFile`
        """
        
        

        self._basic_info = None
        self._file = None
        self.discriminator = None

        self.basic_info = basic_info
        self.file = file

    @property
    def basic_info(self):
        r"""Gets the basic_info of this CreateClusteringJobReq.

        :return: The basic_info of this CreateClusteringJobReq.
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateDrugJobBasicInfo`
        """
        return self._basic_info

    @basic_info.setter
    def basic_info(self, basic_info):
        r"""Sets the basic_info of this CreateClusteringJobReq.

        :param basic_info: The basic_info of this CreateClusteringJobReq.
        :type basic_info: :class:`huaweicloudsdkeihealth.v1.CreateDrugJobBasicInfo`
        """
        self._basic_info = basic_info

    @property
    def file(self):
        r"""Gets the file of this CreateClusteringJobReq.

        :return: The file of this CreateClusteringJobReq.
        :rtype: :class:`huaweicloudsdkeihealth.v1.ClusteringDrugFile`
        """
        return self._file

    @file.setter
    def file(self, file):
        r"""Sets the file of this CreateClusteringJobReq.

        :param file: The file of this CreateClusteringJobReq.
        :type file: :class:`huaweicloudsdkeihealth.v1.ClusteringDrugFile`
        """
        self._file = file

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
        if not isinstance(other, CreateClusteringJobReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
