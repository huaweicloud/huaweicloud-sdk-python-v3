# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GenerateComplexCombineReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'receptor': 'RunReceptorPreprocessReq',
        'ligand': 'ReceptorDrugFileReq'
    }

    attribute_map = {
        'receptor': 'receptor',
        'ligand': 'ligand'
    }

    def __init__(self, receptor=None, ligand=None):
        r"""GenerateComplexCombineReq

        The model defined in huaweicloud sdk

        :param receptor: 
        :type receptor: :class:`huaweicloudsdkeihealth.v1.RunReceptorPreprocessReq`
        :param ligand: 
        :type ligand: :class:`huaweicloudsdkeihealth.v1.ReceptorDrugFileReq`
        """
        
        

        self._receptor = None
        self._ligand = None
        self.discriminator = None

        self.receptor = receptor
        self.ligand = ligand

    @property
    def receptor(self):
        r"""Gets the receptor of this GenerateComplexCombineReq.

        :return: The receptor of this GenerateComplexCombineReq.
        :rtype: :class:`huaweicloudsdkeihealth.v1.RunReceptorPreprocessReq`
        """
        return self._receptor

    @receptor.setter
    def receptor(self, receptor):
        r"""Sets the receptor of this GenerateComplexCombineReq.

        :param receptor: The receptor of this GenerateComplexCombineReq.
        :type receptor: :class:`huaweicloudsdkeihealth.v1.RunReceptorPreprocessReq`
        """
        self._receptor = receptor

    @property
    def ligand(self):
        r"""Gets the ligand of this GenerateComplexCombineReq.

        :return: The ligand of this GenerateComplexCombineReq.
        :rtype: :class:`huaweicloudsdkeihealth.v1.ReceptorDrugFileReq`
        """
        return self._ligand

    @ligand.setter
    def ligand(self, ligand):
        r"""Sets the ligand of this GenerateComplexCombineReq.

        :param ligand: The ligand of this GenerateComplexCombineReq.
        :type ligand: :class:`huaweicloudsdkeihealth.v1.ReceptorDrugFileReq`
        """
        self._ligand = ligand

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
        if not isinstance(other, GenerateComplexCombineReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
