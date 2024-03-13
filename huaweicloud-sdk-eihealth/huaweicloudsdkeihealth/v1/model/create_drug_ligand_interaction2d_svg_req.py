# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateDrugLigandInteraction2dSvgReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'receptor_file': 'ReceptorDrugFileReq',
        'ligand_file': 'DrugFile'
    }

    attribute_map = {
        'receptor_file': 'receptor_file',
        'ligand_file': 'ligand_file'
    }

    def __init__(self, receptor_file=None, ligand_file=None):
        """CreateDrugLigandInteraction2dSvgReq

        The model defined in huaweicloud sdk

        :param receptor_file: 
        :type receptor_file: :class:`huaweicloudsdkeihealth.v1.ReceptorDrugFileReq`
        :param ligand_file: 
        :type ligand_file: :class:`huaweicloudsdkeihealth.v1.DrugFile`
        """
        
        

        self._receptor_file = None
        self._ligand_file = None
        self.discriminator = None

        self.receptor_file = receptor_file
        if ligand_file is not None:
            self.ligand_file = ligand_file

    @property
    def receptor_file(self):
        """Gets the receptor_file of this CreateDrugLigandInteraction2dSvgReq.

        :return: The receptor_file of this CreateDrugLigandInteraction2dSvgReq.
        :rtype: :class:`huaweicloudsdkeihealth.v1.ReceptorDrugFileReq`
        """
        return self._receptor_file

    @receptor_file.setter
    def receptor_file(self, receptor_file):
        """Sets the receptor_file of this CreateDrugLigandInteraction2dSvgReq.

        :param receptor_file: The receptor_file of this CreateDrugLigandInteraction2dSvgReq.
        :type receptor_file: :class:`huaweicloudsdkeihealth.v1.ReceptorDrugFileReq`
        """
        self._receptor_file = receptor_file

    @property
    def ligand_file(self):
        """Gets the ligand_file of this CreateDrugLigandInteraction2dSvgReq.

        :return: The ligand_file of this CreateDrugLigandInteraction2dSvgReq.
        :rtype: :class:`huaweicloudsdkeihealth.v1.DrugFile`
        """
        return self._ligand_file

    @ligand_file.setter
    def ligand_file(self, ligand_file):
        """Sets the ligand_file of this CreateDrugLigandInteraction2dSvgReq.

        :param ligand_file: The ligand_file of this CreateDrugLigandInteraction2dSvgReq.
        :type ligand_file: :class:`huaweicloudsdkeihealth.v1.DrugFile`
        """
        self._ligand_file = ligand_file

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
        if not isinstance(other, CreateDrugLigandInteraction2dSvgReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
