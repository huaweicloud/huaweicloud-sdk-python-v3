# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAdmetJobReq:

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
        'molecule_file': 'MoleculeFileDto',
        'model_ids': 'list[str]'
    }

    attribute_map = {
        'basic_info': 'basic_info',
        'molecule_file': 'molecule_file',
        'model_ids': 'model_ids'
    }

    def __init__(self, basic_info=None, molecule_file=None, model_ids=None):
        """CreateAdmetJobReq

        The model defined in huaweicloud sdk

        :param basic_info: 
        :type basic_info: :class:`huaweicloudsdkeihealth.v1.CreateDrugJobBasicInfo`
        :param molecule_file: 
        :type molecule_file: :class:`huaweicloudsdkeihealth.v1.MoleculeFileDto`
        :param model_ids: 模型id列表
        :type model_ids: list[str]
        """
        
        

        self._basic_info = None
        self._molecule_file = None
        self._model_ids = None
        self.discriminator = None

        self.basic_info = basic_info
        self.molecule_file = molecule_file
        if model_ids is not None:
            self.model_ids = model_ids

    @property
    def basic_info(self):
        """Gets the basic_info of this CreateAdmetJobReq.

        :return: The basic_info of this CreateAdmetJobReq.
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateDrugJobBasicInfo`
        """
        return self._basic_info

    @basic_info.setter
    def basic_info(self, basic_info):
        """Sets the basic_info of this CreateAdmetJobReq.

        :param basic_info: The basic_info of this CreateAdmetJobReq.
        :type basic_info: :class:`huaweicloudsdkeihealth.v1.CreateDrugJobBasicInfo`
        """
        self._basic_info = basic_info

    @property
    def molecule_file(self):
        """Gets the molecule_file of this CreateAdmetJobReq.

        :return: The molecule_file of this CreateAdmetJobReq.
        :rtype: :class:`huaweicloudsdkeihealth.v1.MoleculeFileDto`
        """
        return self._molecule_file

    @molecule_file.setter
    def molecule_file(self, molecule_file):
        """Sets the molecule_file of this CreateAdmetJobReq.

        :param molecule_file: The molecule_file of this CreateAdmetJobReq.
        :type molecule_file: :class:`huaweicloudsdkeihealth.v1.MoleculeFileDto`
        """
        self._molecule_file = molecule_file

    @property
    def model_ids(self):
        """Gets the model_ids of this CreateAdmetJobReq.

        模型id列表

        :return: The model_ids of this CreateAdmetJobReq.
        :rtype: list[str]
        """
        return self._model_ids

    @model_ids.setter
    def model_ids(self, model_ids):
        """Sets the model_ids of this CreateAdmetJobReq.

        模型id列表

        :param model_ids: The model_ids of this CreateAdmetJobReq.
        :type model_ids: list[str]
        """
        self._model_ids = model_ids

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
        if not isinstance(other, CreateAdmetJobReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
