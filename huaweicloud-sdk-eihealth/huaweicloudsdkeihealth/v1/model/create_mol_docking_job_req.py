# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateMolDockingJobReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'receptor': 'ReceptorDto',
        'ligand': 'DrugFile',
        'engine': 'str'
    }

    attribute_map = {
        'receptor': 'receptor',
        'ligand': 'ligand',
        'engine': 'engine'
    }

    def __init__(self, receptor=None, ligand=None, engine=None):
        r"""CreateMolDockingJobReq

        The model defined in huaweicloud sdk

        :param receptor: 
        :type receptor: :class:`huaweicloudsdkeihealth.v1.ReceptorDto`
        :param ligand: 
        :type ligand: :class:`huaweicloudsdkeihealth.v1.DrugFile`
        :param engine: 引擎，默认为AUTODOCK_VINA。
        :type engine: str
        """
        
        

        self._receptor = None
        self._ligand = None
        self._engine = None
        self.discriminator = None

        self.receptor = receptor
        self.ligand = ligand
        if engine is not None:
            self.engine = engine

    @property
    def receptor(self):
        r"""Gets the receptor of this CreateMolDockingJobReq.

        :return: The receptor of this CreateMolDockingJobReq.
        :rtype: :class:`huaweicloudsdkeihealth.v1.ReceptorDto`
        """
        return self._receptor

    @receptor.setter
    def receptor(self, receptor):
        r"""Sets the receptor of this CreateMolDockingJobReq.

        :param receptor: The receptor of this CreateMolDockingJobReq.
        :type receptor: :class:`huaweicloudsdkeihealth.v1.ReceptorDto`
        """
        self._receptor = receptor

    @property
    def ligand(self):
        r"""Gets the ligand of this CreateMolDockingJobReq.

        :return: The ligand of this CreateMolDockingJobReq.
        :rtype: :class:`huaweicloudsdkeihealth.v1.DrugFile`
        """
        return self._ligand

    @ligand.setter
    def ligand(self, ligand):
        r"""Sets the ligand of this CreateMolDockingJobReq.

        :param ligand: The ligand of this CreateMolDockingJobReq.
        :type ligand: :class:`huaweicloudsdkeihealth.v1.DrugFile`
        """
        self._ligand = ligand

    @property
    def engine(self):
        r"""Gets the engine of this CreateMolDockingJobReq.

        引擎，默认为AUTODOCK_VINA。

        :return: The engine of this CreateMolDockingJobReq.
        :rtype: str
        """
        return self._engine

    @engine.setter
    def engine(self, engine):
        r"""Sets the engine of this CreateMolDockingJobReq.

        引擎，默认为AUTODOCK_VINA。

        :param engine: The engine of this CreateMolDockingJobReq.
        :type engine: str
        """
        self._engine = engine

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
        if not isinstance(other, CreateMolDockingJobReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
