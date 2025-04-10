# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RecognizeReceptorPocketReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'mode': 'RecognizeReceptorPocketMode',
        'receptor_file': 'ReceptorDrugFileReq',
        'ligand_file': 'DrugFile',
        'residues': 'list[str]'
    }

    attribute_map = {
        'mode': 'mode',
        'receptor_file': 'receptor_file',
        'ligand_file': 'ligand_file',
        'residues': 'residues'
    }

    def __init__(self, mode=None, receptor_file=None, ligand_file=None, residues=None):
        r"""RecognizeReceptorPocketReq

        The model defined in huaweicloud sdk

        :param mode: 
        :type mode: :class:`huaweicloudsdkeihealth.v1.RecognizeReceptorPocketMode`
        :param receptor_file: 
        :type receptor_file: :class:`huaweicloudsdkeihealth.v1.ReceptorDrugFileReq`
        :param ligand_file: 
        :type ligand_file: :class:`huaweicloudsdkeihealth.v1.DrugFile`
        :param residues: 残基列表，当识别模式为残基时提供
        :type residues: list[str]
        """
        
        

        self._mode = None
        self._receptor_file = None
        self._ligand_file = None
        self._residues = None
        self.discriminator = None

        self.mode = mode
        self.receptor_file = receptor_file
        if ligand_file is not None:
            self.ligand_file = ligand_file
        if residues is not None:
            self.residues = residues

    @property
    def mode(self):
        r"""Gets the mode of this RecognizeReceptorPocketReq.

        :return: The mode of this RecognizeReceptorPocketReq.
        :rtype: :class:`huaweicloudsdkeihealth.v1.RecognizeReceptorPocketMode`
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        r"""Sets the mode of this RecognizeReceptorPocketReq.

        :param mode: The mode of this RecognizeReceptorPocketReq.
        :type mode: :class:`huaweicloudsdkeihealth.v1.RecognizeReceptorPocketMode`
        """
        self._mode = mode

    @property
    def receptor_file(self):
        r"""Gets the receptor_file of this RecognizeReceptorPocketReq.

        :return: The receptor_file of this RecognizeReceptorPocketReq.
        :rtype: :class:`huaweicloudsdkeihealth.v1.ReceptorDrugFileReq`
        """
        return self._receptor_file

    @receptor_file.setter
    def receptor_file(self, receptor_file):
        r"""Sets the receptor_file of this RecognizeReceptorPocketReq.

        :param receptor_file: The receptor_file of this RecognizeReceptorPocketReq.
        :type receptor_file: :class:`huaweicloudsdkeihealth.v1.ReceptorDrugFileReq`
        """
        self._receptor_file = receptor_file

    @property
    def ligand_file(self):
        r"""Gets the ligand_file of this RecognizeReceptorPocketReq.

        :return: The ligand_file of this RecognizeReceptorPocketReq.
        :rtype: :class:`huaweicloudsdkeihealth.v1.DrugFile`
        """
        return self._ligand_file

    @ligand_file.setter
    def ligand_file(self, ligand_file):
        r"""Sets the ligand_file of this RecognizeReceptorPocketReq.

        :param ligand_file: The ligand_file of this RecognizeReceptorPocketReq.
        :type ligand_file: :class:`huaweicloudsdkeihealth.v1.DrugFile`
        """
        self._ligand_file = ligand_file

    @property
    def residues(self):
        r"""Gets the residues of this RecognizeReceptorPocketReq.

        残基列表，当识别模式为残基时提供

        :return: The residues of this RecognizeReceptorPocketReq.
        :rtype: list[str]
        """
        return self._residues

    @residues.setter
    def residues(self, residues):
        r"""Sets the residues of this RecognizeReceptorPocketReq.

        残基列表，当识别模式为残基时提供

        :param residues: The residues of this RecognizeReceptorPocketReq.
        :type residues: list[str]
        """
        self._residues = residues

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
        if not isinstance(other, RecognizeReceptorPocketReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
